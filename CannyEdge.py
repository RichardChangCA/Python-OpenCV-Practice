"""
Canny 边缘提取算法，要求不能是float数据类型
"""
import numpy as np
import cv2 as cv

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0) #降噪，边缘提取算法对噪声敏感
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    #edge_output = cv.Canny(xgrad, ygrad, 50, 150)  #50与150是上下阈值,推荐比例3:1或2：1
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)

    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("Color Edge", dst)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/lb.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()