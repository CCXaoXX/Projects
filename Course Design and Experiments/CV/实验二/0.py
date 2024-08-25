import cv2 as cv
import numpy as np

im = cv.imread('sift/p1.png', cv.IMREAD_GRAYSCALE)
sz = 7
sig = 3
levels = 5

# 构建高斯金字塔
gauss_pyr = [im]
for i in range(levels-1):
    gauss_pyr.append(cv.pyrDown(gauss_pyr[-1]))


# 展示每一层的高斯模糊效果和高斯差分效果
for i in range(levels):
    # 高斯模糊
    blur = cv.GaussianBlur(gauss_pyr[i], (sz, sz), sig)
    cv.imwrite(f"result2/gaussian{i}.png", blur)

    # 高斯差分
    diff = cv.subtract(gauss_pyr[i], blur)
    # 将差分图像归一化至[0, 255]并写入文件
    diff_norm = ((diff - np.min(diff)) / (np.max(diff) - np.min(diff))) * 255
    cv.imwrite(f"result2/diff{i}.png", diff_norm)