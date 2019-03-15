
import numpy as np
import cv2 as cv

def template_demo():
    tpl = cv.imread("C:/Users/46507/Desktop/zlf_tpl.jpg")
    target = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        #print(target.dtype)
        result = cv.matchTemplate(target, tpl, md)
        print(result)
        print(result*255)
        result = result * 255
        result = result.astype(np.uint8)
        print(result)
        cv.imshow("match-" + np.str(md), result)
        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # if md == cv.TM_SQDIFF_NORMED:
        #     tl = min_loc
        # else:
        #     tl = max_loc
        # br = (tl[0]+tw, tl[1]+th)
        # cv.rectangle(target, tl, br, (0, 0, 255), 2)
        #cv.imshow("match-"+np.str(md), target)



print("---hello python---")
src = cv.imread("C:/Users/46507/Desktop/zlf.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
template_demo()
cv.waitKey(0)

cv.destroyAllWindows()