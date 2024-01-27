import cv2
import numpy as np
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'


def find_marks(image, points):
    y = 3366
    x = 2406
    sh = image.shape
    res = []
    for key, value in points.items():
        coord = []
        for i in range(len(value)):
            if value[i] == "-" and i == 0:
                coord.append(0)
            elif value[i] == "-" and i == 1:
                coord.append(image.shape[0])
            elif value[i] == "-" and i == 2:
                coord.append(0)
            elif value[i] == "-" and i == 3:
                coord.append(image.shape[1])
            elif i == 0 or i == 1:
                coord.append(sh[0] - (y - value[i]) + 10)
            else:
                coord.append(sh[1] - (x - value[i]))
        if key == "+":
            hsv_img = cv2.cvtColor(image[coord[0]+5:coord[1]-5, coord[2]+5:coord[3]-5], cv2.COLOR_BGR2HSV)
            result = cv2.inRange(hsv_img, np.array([0, 0, 180], np.uint8), np.array([0, 0, 245], np.uint8))
            lim = 250
        else:
            hsv_img = cv2.cvtColor(image[coord[0]:coord[1], coord[2]:coord[3]], cv2.COLOR_BGR2HSV)
            result = cv2.inRange(hsv_img, np.array([0, 0, 110], np.uint8), np.array([0, 0, 160], np.uint8))
            lim = 200
        moments = cv2.moments(result, 1)
        print(key, moments)
        # dM01 = moments['m01']
        # dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > lim:
            res.append(key)
    return res
