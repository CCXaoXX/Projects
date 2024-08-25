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
            # Y = 
            # U =
            # V =  

            ## 1. save temp_YUV for visualization
            #
            #
            #
            #
            #

            ## 2. enhance Y and convert YUV back to the RGB
            #
            #
            #
            #
            #

            ## 3. store the enhanced RGB
            # 
            #
            #
            #
            #

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
