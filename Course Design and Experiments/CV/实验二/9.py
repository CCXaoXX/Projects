import os
import sys
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 设置图像文件夹路径
imgPath = 'img/'
imgList = os.listdir(imgPath)
imgs = []

# 读取所有图像
for imgName in imgList:
    pathImg = os.path.join(imgPath, imgName)
    img = cv.imread(pathImg)
    if img is None:
        print("图片不能读取：" + imgName)
        sys.exit(-1)
    imgs.append(img)

# 创建 Stitcher 对象
stitcher = cv.Stitcher.create(cv.Stitcher_PANORAMA)

# 拼接图像
result, pano = stitcher.stitch(imgs)

# 判断拼接是否成功
if result == cv.STITCHER_OK:
    # 输出拼接结果
    cv.imwrite('result1/merge.png', pano)
    cv.waitKey(0)
    # 显示所有读取的图像

else:
    print('Error during stitching')

# 销毁所有窗口
cv.destroyAllWindows()