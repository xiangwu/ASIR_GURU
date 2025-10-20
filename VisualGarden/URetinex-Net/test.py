import argparse
import torch
import torch.nn as nn
from network.Math_Module import P, Q
from network.decom import Decom
import os
import torchvision.transforms as transforms
from PIL import Image
import time
from utils import *
import matplotlib.pyplot as plt


def one2three(x):
    return torch.cat([x, x, x], dim=1).to(x)


class Inference(nn.Module):
    def __init__(self, opts):
        super().__init__()
        self.opts = opts

        # 加载模型
        self.model_Decom_low = Decom()
        self.model_Decom_low = load_initialize(self.model_Decom_low, self.opts.Decom_model_low_path)

        self.unfolding_opts, self.model_R, self.model_L = load_unfolding(self.opts.unfolding_model_path)
        self.adjust_model = load_adjustment(self.opts.adjust_model_path)

        self.P = P()
        self.Q = Q()

        transform = [transforms.ToTensor()]
        self.transform = transforms.Compose(transform)

        print(self.model_Decom_low)
        print(self.model_R)
        print(self.model_L)
        print(self.adjust_model)

    def unfolding(self, input_low_img):
        for t in range(self.unfolding_opts.round):
            if t == 0:
                P, Q = self.model_Decom_low(input_low_img)
            else:
                w_p = (self.unfolding_opts.gamma + self.unfolding_opts.Roffset * t)
                w_q = (self.unfolding_opts.lamda + self.unfolding_opts.Loffset * t)
                P = self.P(I=input_low_img, Q=Q, R=R, gamma=w_p)
                Q = self.Q(I=input_low_img, P=P, L=L, lamda=w_q)
            R = self.model_R(r=P, l=Q)
            L = self.model_L(l=Q)
        return R, L

    def lllumination_adjust(self, L, ratio):
        ratio = torch.ones(L.shape).cuda() * self.opts.ratio
        return self.adjust_model(l=L, alpha=ratio)

    def forward(self, input_low_img):
        if torch.cuda.is_available():
            input_low_img = input_low_img.cuda()
        with torch.no_grad():
            start = time.time()
            R, L = self.unfolding(input_low_img)
            High_L = self.lllumination_adjust(L, self.opts.ratio)
            I_enhance = High_L * R
            p_time = (time.time() - start)
        return I_enhance, p_time

    def run(self, low_img_path):
        file_name = os.path.basename(low_img_path)
        name = os.path.splitext(file_name)[0]

        # 加载图像
        low_img = self.transform(Image.open(low_img_path).convert('RGB')).unsqueeze(0)
        enhance, p_time = self.forward(input_low_img=low_img)

        # 可视化并保存结果
        low_img_np = low_img.squeeze().cpu().numpy().transpose(1, 2, 0)
        enhance_np = enhance.squeeze().cpu().numpy().transpose(1, 2, 0)

        # 可选：禁用图像弹窗避免阻塞批处理
        # plt.figure(figsize=(12, 6))
        # plt.subplot(1, 2, 1)
        # plt.imshow(low_img_np)
        # plt.title('Input Image')
        # plt.axis('off')
        # plt.subplot(1, 2, 2)
        # plt.imshow(enhance_np)
        # plt.title('Enhanced Image')
        # plt.axis('off')
        # plt.show()
        # plt.close()

        os.makedirs(self.opts.output, exist_ok=True)
        output_path = os.path.join(self.opts.output, f"{name}_enhanced.png")
        enhance_img = (enhance_np * 255.0).clip(0, 255).astype('uint8')
        Image.fromarray(enhance_img).save(output_path)

        print(f"[{file_name}] enhanced in {p_time:.3f}s → saved to: {output_path}")

    def run_folder(self, folder_path):
        supported_exts = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        image_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[-1].lower() in supported_exts]

        if not image_files:
            print(f"No images found in {folder_path}")
            return

        for fname in image_files:
            img_path = os.path.join(folder_path, fname)
            self.run(img_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Enhancement (Batch Supported)')
    parser.add_argument('--img_path', type=str, default="./demo/input", help="Path to image or folder")
    parser.add_argument('--output', type=str, default="./demo/output")
    parser.add_argument('--ratio', type=int, default=5)
    parser.add_argument('--Decom_model_low_path', type=str, default="./ckpt/init_low.pth")
    parser.add_argument('--unfolding_model_path', type=str, default="./ckpt/unfolding.pth")
    parser.add_argument('--adjust_model_path', type=str, default="./ckpt/L_adjust.pth")
    parser.add_argument('--gpu_id', type=int, default=0)

    opts = parser.parse_args()
    for k, v in vars(opts).items():
        print(k, v)

    os.environ['CUDA_VISIBLE_DEVICES'] = str(opts.gpu_id)
    model = Inference(opts).cuda()

    if os.path.isdir(opts.img_path):
        model.run_folder(opts.img_path)  # 批处理整个文件夹
    else:
        model.run(opts.img_path)         # 单图增强
