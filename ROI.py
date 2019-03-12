"""
ROI
泛洪填充
"""

import numpy as np
import cv2 as cv

def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyImg, mask, (300, 50), (0, 255, 255), (60, 60, 60), (60, 60, 60), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImg)

def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("fill_binary", image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY) #BGR通道
    cv.imshow("filled binary", image)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#fill_color_demo(src)
fill_binary()
# face = src[50:500, 100:300] #height ,width, ROI(Region of Interest)
# gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
# backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# cv.imshow("backface", backface) #still gray
# src[50:500, 100:300] = backface  #padding
# cv.imshow("face", src)
cv.waitKey(0)

cv.destroyAllWindows()