"""
模糊操作：均值模糊，中值模糊，自定义模糊
基于离散卷积，定义好每个卷积核，不同卷积核得到不同的卷积效果，模糊是卷积的一种表象
"""

from numpy import *
import cv2 as cv
import numpy as np

#定义添加椒盐噪声的函数
def SaltAndPepper(src,percetage):
    SP_NoiseImg=src
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randX=random.randint(0, src.shape[0]-1)
        randY=random.randint(0, src.shape[1]-1)
        if random.randint(0, 1) == 0:
            SP_NoiseImg[randX, randY] = 0
        else:
            SP_NoiseImg[randX, randY] = 255
    return SP_NoiseImg

def blur_demo(image):  #均值模糊，随机去噪
    dst = cv.blur(image, (50, 50))  #卷积核1行3列
    cv.imshow("blur_demo", dst)

def median_blur_demo(image): #中值模糊-降噪，椒盐噪声
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)

def custom_blur_demo(image):
    #kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9
    #kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel = kernel) #-1默认ddepth
    cv.imshow("custom_blur_demo", dst)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#blur_demo(src)
# src_noise = SaltAndPepper(src, 0.1)
# # cv.imshow("Salt_and_Pepper", src_noise)
# # median_blur_demo(src_noise)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
