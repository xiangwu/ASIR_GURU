import torch
import torchvision
from PIL import Image
import numpy as np
import os
import net  # 确保 net.py 在同一目录下


def dehaze_single_image(image_path, save_dir="results", model_path="snapshots/dehazer.pth"):
    """
    对单张图片进行去雾处理，仅保存去雾后的结果
    """
    # 判断是否使用GPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # 自动创建保存目录
    os.makedirs(save_dir, exist_ok=True)

    # 读取并预处理图片
    data_hazy = Image.open(image_path).convert('RGB')
    data_hazy = np.asarray(data_hazy) / 255.0
    data_hazy = torch.from_numpy(data_hazy).float().permute(2, 0, 1).unsqueeze(0).to(device)

    # 加载模型
    dehaze_net = net.dehaze_net().to(device)
    dehaze_net.load_state_dict(torch.load(model_path, map_location=device))
    dehaze_net.eval()

    # 推理
    with torch.no_grad():
        clean_image = dehaze_net(data_hazy)

    # 保存结果（只保存去雾后图片）
    filename = os.path.basename(image_path)
    save_path = os.path.join(save_dir, filename)
    torchvision.utils.save_image(clean_image, save_path)

    print(f"✅ Dehazed image saved at: {save_path}")


if __name__ == "__main__":
    # ✳️ 修改为你想处理的图片路径
    image_path = "test_images/canyon.png"
    dehaze_single_image(image_path)
