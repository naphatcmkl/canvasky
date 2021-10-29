import cv2
import numpy as np
import os
import time
from cvzone.HandTrackingModule import HandDetector

# Set webcam capture from USB PORT 0
capture = cv2.VideoCapture(0)

# Add hand detector
detector = HandDetector(detectionCon=1)

# Set webcam capture window size as 1280x720
capture.set(3, 1280)
capture.set(4, 720)


while True:
    # 1. Read capture
    success, img = capture.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img, draw=False)
    cv2.imshow("Canvas", img)
    if cv2.waitKey(1) == ord('q'):
        break

    # lmList = detector.findPosition(img, draw=False)

    # if len(lmList) != 0:

    #     fingersx = detector.fingersUp()
    #     print(fingersx)

    # print(lmList)


    if fingers == [0, 0, 0, 1, 0]:
        print("draw")
    elif fingers == [0, 0, 1, 1, 0]:
        print("erase")


#voice reg: color, size
#hand: pen, eraser, capture