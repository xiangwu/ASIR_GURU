# 暗光图像增强算法整理 — URetinex-Net

% 本项目整理并复现了 **URetinex-Net: Retinex-based Deep Unfolding Network for Low-Light Image Enhancement**（CVPR 2022）算法。  
% 该算法基于 **Retinex 理论**，通过深度展开结构实现低光照图像的亮度恢复与细节增强。
% 2025.10 Original written by Yang Tianrui 杨甜蕊.
---

## 📖 论文与资源
- 📄 [论文原文（CVPR 2022）](https://openaccess.thecvf.com/content/CVPR2022/papers/Wu_URetinex-Net_Retinex-Based_Deep_Unfolding_Network_for_Low-Light_Image_Enhancement_CVPR_2022_paper.pdf)
- 📘 [补充材料](https://openaccess.thecvf.com/content/CVPR2022/supplemental/Wu_URetinex-Net_Retinex-Based_Deep_CVPR_2022_supplemental.pdf)
- 🎥 [演示视频](https://www.youtube.com/watch?v=MJZ5HT1jGrA)


---

## 🛠️ 环境要求（Requirements）

| 环境 | 版本 |
|------|------|
| Python | 3.7.6 |
| PyTorch | 1.4.0 |
| torchvision | 0.5.0 |

安装方式：
```bash
pip install torch==1.4.0 torchvision==0.5.0


---

## 🛠️ 使用方法

## 快速测试一张图片
python test.py --img_path "./demo/input/img.png"
程序会自动将增强后的结果保存到：

./demo/output/

## 💾 预训练模型（Pretrained Model）

若要在论文使用的 LOL 数据集 上评估预训练模型：
下载数据集（包含低光图像与参考增强图像）：
🔗 LOL dataset 官方地址

按如下结构放置：
./test_data/LOLdataset/eval15/

运行：
python evaluate.py

结果将自动保存并输出 PSNR/SSIM 等指标。

作者在论文中提供了预训练权重，可从原始仓库下载（或根据需要自行训练）。


## 📚 引用（Citation）

如果你使用了 URetinex-Net 的算法或代码，请引用原论文：

```
@InProceedings{Wu_2022_CVPR,
    author    = {Wu, Wenhui and Weng, Jian and Zhang, Pingping and Wang, Xu and Yang, Wenhan and Jiang, Jianmin},
    title     = {URetinex-Net: Retinex-Based Deep Unfolding Network for Low-Light Image Enhancement},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2022},
    pages     = {5901-5910}
}
```