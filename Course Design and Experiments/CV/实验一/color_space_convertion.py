import numpy as np
import cv2
import math
import os

def RGB2YUV_enhance(img, lightness_en=3.5):
    temp_YUV = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    res_RGB  = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    timg = img.astype(np.float32)
    for i in range(timg.shape[0]):
        for j in range(timg.shape[1]):
            ##############################################################
            # Note that, should be careful about the RGB or BGR order
            # Hint: check the transformation matrix to convert RGB to YUV
            ##############################################################
            ## write your code here
            # Y = 0.2990R+0.5870G+0.1140B
            # U = -0.1684R-0.3316G+0.5B+128
            # V = 0.5R-0.4187G-0.0813B+128
            # R = Y + 1.4075 * V
            # G = Y - 0.3455 * U - 0.7169 * V
            # B = Y + 1.779 * U
            ## 1. save temp_YUV for visualization
            Y = 0.2990*timg[i][j][0] + 0.5870*timg[i][j][1] + 0.1140* timg[i][j][2]
            U = -0.1684*timg[i][j][0] -0.3316*timg[i][j][1] + 0.5* timg[i][j][2] + 128
            V = 0.5*timg[i][j][0] - 0.4187*timg[i][j][1] - 0.0813* timg[i][j][2] + 128
            temp_YUV[i][j][0] = Y
            temp_YUV[i][j][1] = U
            temp_YUV[i][j][2] = V

            ## 2. enhance Y and convert YUV back to the RGB
            Y = lightness_en * Y

            R = Y + 1.4075 * V
            G = Y - 0.3455 * U - 0.7169 * V
            B = Y + 1.779 * U

            ## 3. store the enhanced RGB
            res_RGB[i][j][0] = R
            res_RGB[i][j][1] = G
            res_RGB[i][j][2] = B

            #############################################################
            # end of your code
            #############################################################
            pass
            #############################################################
            # (Optional) consider more efficent way to implement such a conversion
            #############################################################
    return temp_YUV, res_RGB



if __name__ == '__main__':
    img = cv2.imread("test/Lena.jpg")
    imgyuv, res_rgb = RGB2YUV_enhance(img)
    cv2.imshow('orginal image', img)
    cv2.imshow('Y', imgyuv[:,:,0])
    cv2.imshow('U', imgyuv[:,:,1])
    cv2.imshow('V', imgyuv[:,:,2])
    cv2.imshow('Enhance Light', res_rgb)
    # cv2.imwrite("rgb2yuv.jpg", imgyuv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
