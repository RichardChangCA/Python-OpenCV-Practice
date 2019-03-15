"""
降采样，还原，高斯金字塔，拉普拉斯金字塔
"""
import numpy as np
import cv2 as cv

def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down_"+str(i), dst)
        temp = dst.copy()
    return pyramid_images

def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    print(level)

    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            #print("lapalian_down_origin", image.shape[:2])
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down_origin", lpls)
        else:
            #print("lapalian_down_"+str(i), pyramid_images[i-1].shape[:2])
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2]) #输入的图像必须2的n次方
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lapalian_down_"+str(i), lpls)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
crop_size = (512, 512)
img = cv.resize(src, crop_size, interpolation=cv.INTER_CUBIC)
#print(img.shape[:2])
#cv.imshow("try", img)
#pyramid_demo(src)
lapalian_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()