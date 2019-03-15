"""
一阶导数，sobel算子，增强版Scharr
sobel算子：水平梯度，垂直梯度
二阶导数，lapalian算子
计算梯度，二阶导数为0（差异最大，导数最大，再导为0）
"""
import numpy as np
import cv2 as cv

def lapalian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])  #两种算子
    #kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo", lpls)

def sobel_demo(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    #grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    #grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#sobel_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()