
import cv2 as cv
import numpy as np

im1 = cv.imread('sift/p1.png')
im2 = cv.imread('sift/p2.png')
sift = cv.SIFT_create()

# 获取各个图像的特征点及sift特征向量
(kp1, des1) = sift.detectAndCompute(im1, None)
(kp2, des2) = sift.detectAndCompute(im2, None)

# 特征点匹配
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# 计算特征点之间的平均欧式距离
distances = []
for m1, m2 in matches:
    if m1.distance < 0.75 * m2.distance:
        distances.append(m1.distance)
mean_distance = np.mean(distances)

print(f"特征点之间的平均欧式距离为 {mean_distance}")