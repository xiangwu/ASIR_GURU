import cv2

# 读取原始RGB图像
img = cv2.imread('D:/pycharmproject/low light/URetinex-Net/demo/input/520.jpg')  # 替换为你的图像路径

# 将图像从BGR转换为LAB（注意OpenCV默认读取为BGR）
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# 提取L通道（亮度）
L_channel = lab[:, :, 0]

# 保存L通道图像
cv2.imwrite('L_channel.jpg', L_channel)
