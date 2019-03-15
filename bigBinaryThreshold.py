"""
二值图像 0&1
"""
import numpy as np
import cv2 as cv

def threshold_demo(image):  #全局阈值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret , binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)  #在0处指定阈值，将 | cv.THRESH_TRIANGLE去掉
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)  #自定义阈值
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)  #与上面转置
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)  #在127处截断
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
    print("threshold value %s" % ret)
    cv.imshow("binary", binary)

def local_threshold(image): #局部二值化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary", binary)

def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum() / (w*h)
    print("mean :", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)  #ret就是mean
    cv.imshow("binary", binary)

def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row: row+ch, col:cw+col]
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 15:
                gray[row:row+ch, col:cw+col] = 255
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row + ch, col:cw + col] = dst
            #dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            #gray[row:row+ch, col:cw+col] = dst
            #print(np.std(dst), np.mean(dst))
    cv.imwrite("C:/Users/46507/Desktop/zlf1.jpg", gray)

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/dog.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#threshold_demo(src)
#local_threshold(src)
#custom_threshold(src)
#big_image_binary(src)
cv.waitKey(0)

cv.destroyAllWindows()