import cv2 as cv
import numpy as np

im = cv.imread('sift/p1.png', cv.IMREAD_GRAYSCALE)
levels = 5
sigma = 1.6
k = 2 ** (1 / levels)

# 构建高斯金字塔
gauss_pyr = [im]
for i in range(levels-1):
    sigma *= k
    sz = int(np.ceil(sigma * 5) * 2 + 1)  # 计算当前层的高斯核大小
    gauss_pyr.append(cv.GaussianBlur(gauss_pyr[-1], (sz, sz), sigma))

# 构建拉普拉斯金字塔
lap_pyr = [cv.subtract(gauss_pyr[-2], gauss_pyr[-1])]
for i in range(levels-2, -1, -1):
    # 当前层的图像
    im = gauss_pyr[i]

    # 计算当前层的高斯核大小和阈值
    sigma = 1.6 * (2 ** i)
    sz = int(np.ceil(sigma * 5) * 2 + 1)
    th = 0.01

    # 计算当前层的 DoG 图像
    dog = cv.absdiff(cv.GaussianBlur(im, (sz, sz), sigma),
                     cv.GaussianBlur(im, (sz, sz), k * sigma))

    # 找到当前层的极值点
    mask = cv.compare(dog, th, cv.CMP_GT)
    extremas = cv.bitwise_and(mask, cv.compare(dog, -th, cv.CMP_LT))

    # 将当前层的极值点用不同颜色标注
    color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (128, 0, 128), (0, 255, 255)]
    for j, ext in enumerate(extremas):
        if ext.any():
            y, x = np.where(ext == 255)
            for x_, y_ in zip(x, y):
                # 根据不同层的颜色标记极值点
                color_index = i % len(color)
                im = cv.circle(im, (x_, y_), 2, color[color_index], -1)

    # 将当前层的标记后的图像显示出来
    cv.imshow('extremas', im)
    cv.waitKey(0)
