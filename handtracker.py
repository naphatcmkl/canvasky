import cv2
import numpy as np
import HandTrackingModule as htm
import time
import os

cap = cv2.VideoCapture(1)
cap.set(3, 1280)


while True:
        success, img = cap.read()
        