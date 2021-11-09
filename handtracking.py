import cv2
import numpy as np
import os,sys
import time
import speech_recognition as sr
from cvzone.HandTrackingModule import HandDetector
from mss import mss
import pygetwindow
import pyautogui
from PIL import Image


r = sr.Recognizer()

control_path = "controlhead"
mycontrol = os.listdir(control_path)
controller_list = []
for index_me in mycontrol:
    image_reader = cv2.imread(f'{control_path}/{index_me}')
    controller_list.append(image_reader)
print("png head file ",controller_list)

control_tab = controller_list[0]
control_tab_off = controller_list[1]
# print("list1 ",control_tab)
# print("list2 ",controller_list[1])

draw_mode = [0, 1, 0, 0, 0]
erase_mode = [0, 1, 1, 0, 0]
idle_mode = [0, 1, 1, 1, 0]
cap_all = [1, 1, 1, 1, 1]
clear_all = [0, 0, 0, 0, 0]
voice_cmd = [1, 1, 0, 0, 1]
blue_color = (255, 0, 0)
black_color = (0, 0, 0)
idk_color = (0, 255, 0)
brush_thick = 20
eraser_thick = 60
canvas_show = 0
running_main = True
over = False
show_tab = True

deb = 0
timer = 0
# Set webcam capture from USB PORT 0
capture = cv2.VideoCapture(0)

# Add hand detector
detector = HandDetector(detectionCon=1)

# Set webcam capture window size as 1280x720
capture.set(3, 1280)
capture.set(4, 720)
x_point, y_point = 0, 0
blackCanvas = np.zeros((720, 1280, 3), np.uint8)

while running_main:
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

        # print(fingers)
        if fingers == draw_mode:
            print("draw")
            # cv2.circle(blackCanvas, (x1, y1), 15, blue_color, cv2.FILLED)
            if x_point == 0 and y_point == 0:
                x_point, y_point = x1, y1
            cv2.line(blackCanvas, (x_point, y_point), (x1, y1), idk_color, brush_thick)
            x_point, y_point = x1, y1

        elif fingers == erase_mode:
            print("erase")
            # cv2.circle(blackCanvas, (x1, y1), 15, black_color, cv2.FILLED)
            if x_point == 0 and y_point == 0:
                x_point, y_point = x1, y1
            cv2.line(blackCanvas, (x_point, y_point), (x1, y1), black_color, eraser_thick)
            x_point, y_point = x1, y1
        elif fingers == cap_all:
            print("capture all")
        elif fingers == idle_mode:
            print("idling")
            print("x1, ",x1," y1 ",y1)
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),idk_color,cv2.FILLED)
            if y1 < 85:
                if 60 < x1 < 100:
                    print("hide")
                    show_tab = False
                elif 160 < x1 < 200:
                    print("save")
                    print("saving...")
                    save_path = 'savecanvas.png'
                    all_titles = pygetwindow.getAllTitles()
                    print(all_titles)
                    save_window = pygetwindow.getWindowsWithTitle('Canvas')[0]
                    xx1 = save_window.left
                    yy1 = save_window.top
                    height_1 = save_window.height
                    width_1 = save_window.width
                    xx2 = xx1 + width_1
                    yy2 = yy1 + height_1
                    pyautogui.screenshot(save_path)
                    im = Image.open(save_path)
                    im = im.crop((xx1,yy1,xx2,yy2))
                    im.save(save_path)
                    print("saved")
                elif 260 < x1 < 350:
                    print("red")
                    idk_color = (51, 51, 255)
                elif 400 < x1 < 480:
                    print("blue")
                    idk_color = (255, 153, 51)
                elif 540 < x1 < 640:
                    print("green")
                    idk_color = (51, 255, 51)
                elif 720 < x1 < 800:
                    print("clear")
                elif 830 < x1 < 865:
                    print("quit")
                    over = True

        elif fingers == voice_cmd:
            print("voice reg")
            with sr.Microphone() as source:
                print("Speak: ")

                # Listen
                audio = r.listen(source)

                try:
                    # Translate word into text
                    text = r.recognize_google(audio)
                    print("You said: ", text)

                    # If the word we say translate == champ,
                    if text == "blue" or text == "bloom" or text == "boo" or text == "blue blue blue" or "blue" in text:
                        # Then print you're here.
                        idk_color = (255, 153, 51)
                        print("Change color to blue")
                    elif text == "green" or text == "clean" or "green" in text:
                        idk_color = (51, 255, 51)
                        print("Change color to green")
                    elif text == "red" or text == "rape" or text == "lead" or text == "late" or text == "rate" or text == "raid" or text == "race" or "red" in text :
                        idk_color = (51, 51, 255)
                        print("Change color to red")
                    elif text == "small" or "small" in text:
                        print("set small brush")
                    elif text == "medium" or "medium" in text:
                        print("set medium brush")
                    elif text == "big" or "big" in text:
                        print("set big brush")
                    elif text == "one" or "one" in text:
                        print("set color slot 1")
                        idk_color = (0, 0, 255)
                    elif text == "two" or "two" in text:
                        print("set color slot 2")
                    elif text == "three" or "three" in text:
                        print("set color slot 3")
                    elif text == "capture" or "capture" in text:
                        with mss() as sct:
                            sct.shot()
                            print("captured")
                    elif text == "save" or "save" in text:
                        print("saving...")
                        save_path = 'savecanvas.png'
                        all_titles = pygetwindow.getAllTitles()
                        print(all_titles)
                        save_window = pygetwindow.getWindowsWithTitle('Canvas')[0]
                        xx1 = save_window.left
                        yy1 = save_window.top
                        height_1 = save_window.height
                        width_1 = save_window.width
                        xx2 = xx1 + width_1
                        yy2 = yy1 + height_1
                        pyautogui.screenshot(save_path)
                        im = Image.open(save_path)
                        im = im.crop((xx1,yy1,xx2,yy2))
                        im.save(save_path)
                        print("saved")
                    elif text == "exit" or "exit" in text:
                        print("exiting...")
                        over = True
                    elif text == "show" or "show" in text:
                        show_tab =True
                    elif text == "blind" or "blind" in text:
                        show_tab =True



                except:
                    print("Sorry, couldn't recognize your voice.")
        

    imgGray = cv2.cvtColor(blackCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, blackCanvas)


    #img[0:103,0:926] = control_tab
    if show_tab == True:
        img[0:98,0:921] = control_tab
        #img[0:1,0:1] = control_tab_off
    else:
        img[0:1,0:1] = control_tab_off
    if canvas_show == 0:
        cv2.imshow("Canvas", img)
    elif canvas_show == 1:
        cv2.imshow("Black", blackCanvas)
    # cv2.imshow("Inv", imgInv)

    if cv2.waitKey(1) == ord('q') or over == True:
        break

    # lmList = detector.findPosition(img, draw=False)

    # if len(lmList) != 0:

    #     fingers = detector.fingersUp()
    #     print(fingers)

    # print(lmList)

# voice reg: color, size
# hand: pen, eraser, capture
