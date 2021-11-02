import cv2
import numpy as np
import os
import time
from cvzone.HandTrackingModule import HandDetector

draw_mode = [0, 1, 0, 0, 0]
erase_mode = [0, 1, 1, 0, 0]
cap_all = [1, 1, 1, 1, 1]
clear_all = [0, 0, 0, 0, 0]
blue_color = (255, 0, 0)
black_color = (0, 0, 0)
idk_color = (0, 255, 0)
brush_thick = 20
eraser_thick = 60

deb = 0
# Set webcam capture from USB PORT 0
capture = cv2.VideoCapture(0)

# Add hand detector
detector = HandDetector(detectionCon=1)

# Set webcam capture window size as 1280x720
capture.set(3, 1280)
capture.set(4, 720)
x_point, y_point = 0, 0
blackCanvas = np.zeros((720, 1280, 3), np.uint8)


while True:
    # 1. Read capture
    success, img = capture.read()

    # 2. Find Hand Landmarks
    hands, img = detector.findHands(img, flipType=True)

    if hands:
        lmList = hands[0]["lmList"]  # List of 21 Landmark points

        fingers = detector.fingersUp(hands[0])
        if len(lmList) != 0:
            x1, y1 = lmList[8][0:]
            x2, y2 = lmList[12][0:]
        # x1, y1 = lmList[21:][1:]
        # x2, y2 = lmList[8:][1:]
        # x1, y1 = lmList[91;8]&#91;1:]
        # x2, y2 = lmList[91;12]&#91;1:]
        # if deb <10:
        #     print("time: ",lmList)
        #     deb += 1
        
        #print(fingers)
        if fingers == draw_mode:
            print("draw")
            #cv2.circle(blackCanvas, (x1, y1), 15, blue_color, cv2.FILLED)
            if x_point == 0 and y_point == 0:
                x_point, y_point = x1, y1
            cv2.line(blackCanvas, (x_point, y_point), (x1, y1), idk_color, brush_thick)
            x_point, y_point = x1, y1

        elif fingers == erase_mode:
            print("erase")
            #cv2.circle(blackCanvas, (x1, y1), 15, black_color, cv2.FILLED)
            if x_point == 0 and y_point == 0:
                x_point, y_point = x1, y1
            cv2.line(blackCanvas, (x_point, y_point), (x1, y1), black_color, eraser_thick)
            x_point, y_point = x1, y1
        elif fingers == cap_all:
            print("capture all")


    imgGray = cv2.cvtColor(blackCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    #print("type img", type(img))
    #print("type imgInv ",type(imgInv))
    #print("type black ",type(blackCanvas))
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, blackCanvas)
    #hello
    cv2.imshow("Canvas", img)
    cv2.imshow("Black", blackCanvas)
    cv2.imshow("Inv", imgInv)

    if cv2.waitKey(1) == ord('q'):
        break

    # lmList = detector.findPosition(img, draw=False)

    # if len(lmList) != 0:

    #     fingersx = detector.fingersUp()
    #     print(fingersx)

    # print(lmList)


#voice reg: color, size
#hand: pen, eraser, capture
