import numpy as np
import cv2
import math
import os

# average smoothing kernel
averageKernel = np.array([[1/9, 1/9, 1/9],
                          [1/9, 1/9, 1/9],
                          [1/9, 1/9, 1/9]]).astype(np.float32)

# gaussian smoothing kernel 
weightedAverageKernel = np.array([[1/16, 2/16, 1/16],
                                  [2/16, 4/16, 2/16],
                                  [1/16, 2/16, 1/16]]).astype(np.float32)
# sharppen kernel 
lapalicanKernel = np.array([[0.0,  -1.0, 0.0],
                            [-1.0,  5.0, -1.0],
                            [0.0,  -1.0, 0.0]]).astype(np.float32)


def getGrayImg(img):
    gray = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    timg = img.astype(np.float32)
    for i in range(timg.shape[0]):
        for j in range(timg.shape[1]):
            # R*0.299 + G*0.587 + B*0.114
            gray_intensity = timg[i][j][0]*0.114 + timg[i][j][1]*0.587  + timg[i][j][2]*0.299
            gray[i][j] = np.round(gray_intensity).astype(np.uint8)
    return gray

def paddingWithZero(img):
    padding_img = np.zeros((img.shape[0] + 2, img.shape[1] + 2), np.uint8)
    padding_img[1: img.shape[0] + 1, 1: img.shape[1] + 1] = img
    return padding_img


def paddingWithNeighbor(img):
    padding_img = np.zeros((img.shape[0] + 2, img.shape[1] + 2), np.uint8)
    padding_img[1: img.shape[0] + 1, 1: img.shape[1] + 1] = img
    for i in range(1, img.shape[0] + 1):
        padding_img[i][0] = img[i - 1][0]  # 第一列
        padding_img[i][img.shape[1] + 1] =  img[i - 1][img.shape[1] - 1] # 最后一列
    
    for i in range(1, img.shape[1] + 1):
        padding_img[0][i] = img[0][i - 1] # 第一行
        padding_img[img.shape[0] + 1][i] = img[img.shape[0] - 1][i - 1] # 第一行
    return padding_img



def Filtering2D(img, filter):
# 申请变量, 存储输出图像大小 
    filtered_img = np.zeros((img.shape[0] - 2, img.shape[1] - 2), np.uint8)
    # img 转变为float 类型
    img = img.astype(np.float32)
    for i in range(0, filtered_img.shape[0]):
        for j in range(0, filtered_img.shape[1]):
            # ###### 这里编程实现统计滤波公式 ##########
            # pixel = ?

            # ############## 结束编程 #############
            filtered_img[i][j] = np.clip(pixel, 0.0, 255.0).astype(np.uint8)

    return filtered_img


def denoisewithOrderStatisticsFilter(img):
    filtered_img = np.zeros((img.shape[0] - 2, img.shape[1] - 2), np.uint8)
    for i in range(0, filtered_img.shape[0]):
        for j in range(0, filtered_img.shape[1]):
            # ###### 这里编程实现统计数据公式 ##########
            # pixel = ?
            #
            #
            #
            #
            # ############## 结束编程 #############
            filtered_img[i][j] = pixel
    return filtered_img


def getPSNR(ori_img, en_img):
    MAX = 255
    total = 0
    ori_img = ori_img.astype(np.float32)
    en_img = en_img.astype(np.float32)
    for i in range(ori_img.shape[0]):
        for j in range(ori_img.shape[1]):
            total = total + (ori_img[i][j] - en_img[i][j])**2
    MSE = total / (ori_img.shape[0] * ori_img.shape[1])
    PSNR = 10 * math.log(MAX * MAX / MSE, 10)
    return PSNR



if __name__ == '__main__':
    # 1. 从test文件夹中选一张图进行平滑低通滤波
    img = cv2.imread("test/1_smooth.jpg")
    img = getGrayImg(img)
    cv2.imshow('orginal image', img)
    img_padding = paddingWithNeighbor(img)
    filtered_img = Filtering2D(img_padding, weightedAverageKernel)
    cv2.imshow('filtered image', filtered_img)
    cv2.imwrite("1_enhanced.jpg", filtered_img)
    # 2. 将平滑后的图像行锐化高通滤波 查看结果
    # 
    #
    #
    #
    # 3. 利用均值、中值、最大值、最小值对椒盐、椒、盐噪声图像进行去噪 并 查看结果
    #
    #
    # 
    #
    #
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(getPSNR(img, filtered_img))
