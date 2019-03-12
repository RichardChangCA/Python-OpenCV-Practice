"""
边缘保留滤波EPF，两点像素很大，就很有可能是边缘，就不要平滑
高斯双边模糊
"""
import numpy as np
import cv2 as cv

def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)

def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
