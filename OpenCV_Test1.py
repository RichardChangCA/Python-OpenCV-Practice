import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)  # 0代表摄像头 0可以用视频路径代替，读出的视频没有声音，为了识别，大小有限制
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)  # 左右颠倒
        cv.imshow("video", frame)
        c = cv.waitKey(50)  # 等待50ms
        if c == 27:  # 按Esc退出 ASCII
            break


def get_image_info(image):
    print(image.shape)  # 图像的高 宽 通道数
    print(image.size)
    print(image.dtype)  # 字节位数
    print(type(image))
    pixel_data = np.array(image)
    print(pixel_data)


def access_pixels(image):  # 修改每个像素的值
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]  # 三个通道
    print("width : %s, height : %s channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image):  # 像素转换，与access_pixels效果一样,多调用python的api
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def create_image():
    # img = np.zeros([400, 400, 3], np.uint8)  #三通道
    # img[:, :, 0] = np.ones([400, 400]) * 255  # 变蓝，前面的：默认整体
    # img = np.zeros([400, 400, 1], np.uint8)  # 单通道
    # img[:, :, 0] = np.ones([400, 400])*128  #灰度图
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 128
    cv.imshow("new image", img)


def create_small_image():
    m1 = np.ones([3, 3], np.uint8)
    m1.fill(12222.388)  # 溢出，截断，变成190
    print(m1)
    m2 = m1.reshape([1, 9])
    print(m2)

    m3 = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]], np.uint32)  # 二维数组
    m3.fill(9)
    print(m3)  # 全变成9


def color_space_demo(image):  # 色彩空间转换
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)  # Linux系统上默认颜色空间
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)


def extrace_object_demo(): #颜色追踪
    capture = cv.VideoCapture("C:/Users/46507/Desktop/video_demo.mp4")
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([100, 43, 46])  #识别蓝色
        upper_hsv = np.array([124, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask = mask)
        cv.imshow("video", frame)
        #cv.imshow("mask", mask)
        cv.imshow("dst", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


"""
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")  # RGB
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
"""
# get_image_info(src)
# cv.imwrite("C:/Users/46507/Desktop/zlf_1.jpg", src)
# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.imwrite("C:/Users/46507/Desktop/zlf_2.jpg", gray)
# video_demo()
# t1 = cv.getTickCount()
# access_pixels(src)
# inverse(src)
# t2 = cv.getTickCount() #计时间
# time_spending = (t2-t1)/cv.getTickFrequency()
# print("time : %s ms"%(time_spending * 1000))
# create_image()
# create_small_image()
# color_space_demo(src)
#extrace_object_demo()
"""
b, g, r = cv.split(src)  #通道分离
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
src[:, :, 2] = 0  #第三个通道为0
cv.imshow("changed image", src)
src = cv.merge([b, g, r])  #三个通道合并
"""

def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)

def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)

def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiple_demo", dst)

def others(m1, m2):
    #M1 = cv.mean(m1)  #求均值
    #M2 = cv.mean(m2)
    '''
    M1, dev1 = cv.meanStdDev(m1)  #求均值与方差
    M2, dev2 = cv.meanStdDev(m2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)
    '''
    h, w = m1.shape[:2]
    img = np.zeros([h, w], np.uint8)
    cv.imshow("black", img)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


def logic_demo_and(m1, m2):  #图片位逻辑运算
    dst = cv.bitwise_and(m1, m2)
    cv.imshow("logic_demo_and", dst)

def logic_demo_or(m1, m2):
    dst = cv.bitwise_or(m1, m2)
    cv.imshow("logic_demo_or", dst)

def logic_demo_not(m1):
    dst = cv.bitwise_not(m1)
    cv.imshow("logic_demo_not", dst)

def contrast_brightness_demo(image, c, b):  #改变亮度、对比度
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)

src1 = cv.imread("C:/Users/46507/Desktop/img1.jpg")  # RGB
#cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
x, y = src1.shape[0:2]
src1 = cv.resize(src1, (int(y / 8), int(x / 8)))
#cv.imshow("image1", src1)
#print(src1.shape)
src2 = cv.imread("C:/Users/46507/Desktop/img2.jpg")  # RGB
#cv.namedWindow("image2", cv.WINDOW_AUTOSIZE)
x, y = src2.shape[0:2]
src2 = cv.resize(src2, (int(y / 8), int(x / 8)))
#cv.imshow("image2", src2)
#print(src2.shape)
'''
add_demo(src1, src2)
subtract_demo(src1, src2)
divide_demo(src1, src2)
multiply_demo(src1, src2)
'''

'''
logic_demo_and(src1, src2)
logic_demo_or(src1, src2)
logic_demo_not(src1)
'''
#others(src1, src2)
#contrast_brightness_demo(src1, 1.2, 10)
cv.waitKey(0)  # 无限等待
cv.destroyAllWindows()
