# 图像去雾算法整理 — AOD-Net

本项目基于 **PyTorch** 实现了单幅图像去雾算法 **AOD-Net: All-in-One Dehazing Network**。  
AOD-Net 是一种轻量级端到端网络，通过自适应学习大气散射模型参数，实现图像的快速去雾与细节恢复。  
模型体积小于 **10 KB**，在多种室外/室内数据集上均表现出良好效果。

---

## 📖 论文与资源
- 📄 [论文原文（ICCV 2017）](https://openaccess.thecvf.com/content_iccv_2017/html/Li_AOD-Net_All-In-One_Dehazing_ICCV_2017_paper.html)  
- 📘 [作者主页与数据集](https://sites.google.com/site/boyilics/website-builder/project-page)

---

## 🛠️ 环境要求（Requirements）

| 环境 | 版本 |
|------|------|
| Python | 3.x |
| PyTorch | 0.4 |
| CUDA | 可选（推荐用于加速训练） |

安装方式：
```bash
pip install torch==0.4.0
```

## 🛠️ 使用方法（Testing）

使用预训练模型直接对图像去雾：
预训练模型已包含在 snapshots 文件夹中。

1. 运行 dehaze.py文件，用于批量处理图像
程序会：
从 test_images 文件夹中读取输入图像；

去雾后的结果保存到 results 文件夹中；

2. 运行 test.py文件，用于单张图像测试
程序会：

从 你指定的路径中读取输入图像；

去雾后的结果保存到 results 文件夹中；



## 🚀 模型训练（Training）      

📂 数据准备（Dataset Preparation）
新建文件夹 data
从原作者的项目页面下载并解压数据集至 data 文件夹中：
🔗 下载地址

运行以下命令开始训练：

python train.py


每个训练周期结束后，验证结果会自动保存到 samples 文件夹中。

模型权重文件（快照）会保存到 snapshots 文件夹中。

## 📚 引用（Citation）

若您在研究中使用了 AOD-Net 或本项目的相关代码，请引用以下论文：

```
@InProceedings{Li_2017_ICCV,
    author    = {Li, Boyi and Peng, Xiulian and Wang, Zhangyang and Xu, Jizheng and Feng, Dan},
    title     = {AOD-Net: All-in-One Dehazing Network},
    booktitle = {Proceedings of the IEEE International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2017},
    pages     = {4770-4778}
}
```

## 贡献者
杨甜蕊，邓海英