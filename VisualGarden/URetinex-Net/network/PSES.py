from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import numpy as np
import cv2

# 读取图像
gt = cv2.imread("D:/pycharmproject/low light/URetinex-Net/1.jpg")
dark = cv2.imread("D:/pycharmproject/low light/URetinex-Net/520.jpg")
enhanced = cv2.imread("D:/pycharmproject/low light/URetinex-Net/520_enhanced.png")

# 确保图像尺寸一致
assert gt.shape == dark.shape == enhanced.shape, "图像尺寸不一致！"

# 转灰度（float32 格式），并归一化到 [0,1]
gray_gt = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
gray_dark = cv2.cvtColor(dark, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
gray_enhanced = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

# 增强前 vs Ground Truth
mae_before = np.mean(np.abs(gray_dark - gray_gt))
psnr_before = psnr(gray_gt, gray_dark, data_range=1.0)
ssim_before = ssim(gray_gt, gray_dark, data_range=1.0)

# 增强后 vs Ground Truth
mae_after = np.mean(np.abs(gray_enhanced - gray_gt))
psnr_after = psnr(gray_gt, gray_enhanced, data_range=1.0)
ssim_after = ssim(gray_gt, gray_enhanced, data_range=1.0)

# 打印结果
print("增强前 vs Ground Truth:")
print(f"  MAE: {mae_before:.4f}")
print(f"  PSNR: {psnr_before:.4f}")
print(f"  SSIM: {ssim_before:.4f}")

print("\n增强后 vs Ground Truth:")
print(f"  MAE: {mae_after:.4f}")
print(f"  PSNR: {psnr_after:.4f}")
print(f"  SSIM: {ssim_after:.4f}")
