"""
histogram 一维与多维
直方图均衡化都是灰度图（调整图像对比度，提高图像清晰度，图像增强的方法）
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("直方图")

def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show("RGB直方图")

def equalHist_demo(image):  #全局
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)

def clahe_demo(image):  #局部，适当调大对比度
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)

def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist

def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离：%s，相关性：%s，卡方：%s" % (match1, match2, match3))

def back_projection_demo():
    sample = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
    target = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    cv.imshow("sample", sample)
    cv.imshow("target", target)
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)

def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    #cv.imshow("hist2D", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")

print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
hist2d_demo(src)
#back_projection_demo()
#plot_demo(src)
#image_hist(src)
#img1 = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
#img2 = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
#cv.imshow("image1", img1)
#cv.imshow("image2", img2)
#hist_compare(img1, img2)
#equalHist_demo(src)
#clahe_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
