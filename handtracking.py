import cv2
import numpy as np
import os
import sys
import time
import speech_recognition as sr
from cvzone.HandTrackingModule import HandDetector
from mss import mss
import pygetwindow
import pyautogui
from PIL import Image
import threading

x_point, y_point = 0, 0
brush_thick = 20
eraser_thick = 60
idk_color = (0, 255, 0)
mode = "n"
over = False
show_tab = True
activate_voice_command = False
eraser_color = (0, 0, 0)
voic_user = False
always_on = False


def main():
    global x_point, y_point, mode, brush_thick, eraser_thick, idk_color, over, show_tab, activate_voice_command, eraser_color
    control_path = "controlhead"
    mycontrol = os.listdir(control_path)
    controller_list = []
    check_list = []
    for index_me in mycontrol:
        image_reader = cv2.imread(f'{control_path}/{index_me}')
        check_list.append(index_me)
        controller_list.append(image_reader)
    print("checl: ", check_list)
    # print("png head file ",controller_list)

    control_tab = controller_list[0]
    control_tab_off = controller_list[1]
    # print("list1 ",control_tab)
    # print("list2 ",controller_list[1])

    draw_mode = [0, 1, 0, 0, 0]
    erase_mode = [0, 1, 1, 1, 0]
    idle_mode = [0, 1, 1, 0, 0]
    cap_all = [1, 1, 1, 1, 1]
    clear_all = [0, 0, 0, 0, 0]
    voice_cmd = [1, 1, 0, 0, 1]
    blue_color = (255, 0, 0)
    
    canvas_show = 0
    running_main = True

    deb = 0
    timer = 0
    # Set webcam capture from USB PORT 0
    capture = cv2.VideoCapture(0)

    # Add hand detector
    detector = HandDetector(detectionCon=1)

    # Set webcam capture window size as 1280x720
    capture.set(3, 1280)
    capture.set(4, 720)
    global black_canvas
    black_canvas = np.zeros((720, 1280, 3), np.uint8)

    while running_main:
        # 1. Read capture

        success, img = capture.read()

        #  2. Find Hand Landmarks
        hands, img = detector.findHands(img, flipType=True)
        #  img = cv2.flip(img, 1)

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
                if mode != "d":
                    x_point, y_point = 0, 0
                    mode = "d"
                # cv2.circle(black_canvas, (x1, y1), 15, blue_color, cv2.FILLED)
                if x_point == 0 and y_point == 0:
                    x_point, y_point = x1, y1
                cv2.line(black_canvas, (x_point, y_point), (x1, y1), idk_color, brush_thick)
                x_point, y_point = x1, y1

            elif fingers == erase_mode:
                print("erase")
                if mode != "e":
                    x_point, y_point = 0, 0
                    mode = "e"
                # cv2.circle(black_canvas, (x1, y1), 15, black_color, cv2.FILLED)
                if x_point == 0 and y_point == 0:
                    x_point, y_point = x1, y1
                cv2.line(black_canvas, (x_point, y_point), (x1, y1), eraser_color, eraser_thick)
                x_point, y_point = x1, y1
            elif fingers == cap_all:
                if mode != "c":
                    x_point, y_point = 0, 0
                    mode = "c"

                print("capture all")
            elif fingers == voice_cmd:
                activate_voice_command = True
                print("turn voice cmd on: ", activate_voice_command)
            elif fingers == idle_mode:
                print("idling")
                if mode != "i":
                    x_point, y_point = 0, 0
                    mode = "i"
                print("x1, ", x1, " y1 ", y1)
                cv2.rectangle(img, (x1 - 40, y1 - 40), (x2 + 40, y2 + 40), idk_color, cv2.FILLED)
                if show_tab is True:
                    if y1 < 85:
                        if 60 < x1 < 100:
                            global album_empty
                            print("hide")
                            show_tab = False
                        elif 160 < x1 < 200:
                            print("saving...")
                            all_titles = pygetwindow.getAllTitles()
                            print(all_titles)
                            album = os.listdir("gallery")
                            all_pic = []
                            for each_pic in album:
                                all_pic.append(each_pic)
                            album_empty = False
                            if len(all_pic) <= 0:
                                album_empty = True
                                save_directory = 'gallery/canvas1.png'
                            else:
                                all_int = []
                                for i in range(len(all_pic)):
                                    full = all_pic[i]
                                    cut_first = full[6:]
                                    all_int.append(int(cut_first[:-4]))
                                save_directory = 'gallery/canvas' + str(max(all_int) + 1) + '.png'
                            save_window = pygetwindow.getWindowsWithTitle('Canvas')[0]
                            xx1 = save_window.left
                            yy1 = save_window.top
                            height_1 = save_window.height
                            width_1 = save_window.width
                            xx2 = xx1 + width_1
                            yy2 = yy1 + height_1
                            global save_path
                            save_path = 'gallery' 
                            pyautogui.screenshot(save_directory)
                            im = Image.open(save_directory)
                            im = im.crop((xx1, yy1, xx2, yy2))
                            im.save(save_directory)
                        elif 260 <= x1 <= 350:
                            print("red")
                            idk_color = (51, 51, 255)
                        elif 400 <= x1 <= 480:
                            print("blue")
                            idk_color = (255, 153, 51)
                        elif 540 <= x1 <= 640:
                            print("green")
                            idk_color = (51, 255, 51)
                        elif 720 <= x1 <= 800:
                            print("clear")
                            cv2.rectangle(black_canvas, (0, 0), (1280, 720), eraser_color, cv2.FILLED, )
                        elif 830 <= x1 <= 865:
                            print("quit")
                            over = True

            # elif fingers == voice_cmd:
            #

            else:
                if mode != "n":
                    x_point, y_point = 0, 0
                    mode = "n"

        imgGray = cv2.cvtColor(black_canvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, black_canvas)

        # img[0:103,0:926] = control_tab
        if show_tab is True:
            img[0:98, 0:921] = control_tab
            # img[0:1,0:1] = control_tab_off
        else:
            img[0:1, 0:1] = control_tab_off
        if canvas_show == 0:
            cv2.imshow("Canvas", img)
        elif canvas_show == 1:
            cv2.imshow("Canvas", black_canvas)
        # cv2.imshow("Inv", imgInv)

        if cv2.waitKey(1) == ord('q') or over is True:
            print("exited")
            break

        # lmList = detector.findPosition(img, draw=False)

        # if len(lmList) != 0:

        #     fingers = detector.fingersUp()
        #     print(fingers)

        # print(lmList)

    # voice reg: color, size
    # hand: pen, eraser, capture


def voice_command():
    global x_point, y_point, mode, brush_thick, eraser_thick, idk_color, over, show_tab, activate_voice_command, eraser_color, black_canvas, voic_user, album_empty, save_path, always_on
    r = sr.Recognizer()
    print("using voice..")
    while True:
        print("in voice def")
        print("voic status: ", activate_voice_command, " always: ", always_on)
        if activate_voice_command or always_on:
            

            if mode != "v":
                x_point, y_point = 0, 0
                mode = "v"
            with sr.Microphone() as source:
                print("Speak: ")

                # Listen
                audio = r.listen(source)

                try:
                    # Translate word into text
                    heard = r.recognize_google(audio)
                    text = heard.lower()
                    print("You said: ", text)

                    # If the word we say translate == champ,
                    if text == "blue" or text == "bloom" or text == "boo" or "blue" in text:
                        # Then print you're here.
                        idk_color = (255, 153, 51)
                        print("Change color to blue")
                        activate_voice_command = False
                    elif text == "green" or text == "clean" or "green" in text:
                        idk_color = (51, 255, 51)
                        print("Change color to green")
                        activate_voice_command = False
                    elif text == "red" or text == "rape" or text == "lead" or text == "late" or text == "rate" \
                            or text == "raid" or text == "laid" or text == "race" or "red" in text:
                        idk_color = (51, 51, 255)
                        print("Change color to red")
                        activate_voice_command = False
                    elif text == "tiny" or "tiny" in text:
                        print("set tiny brush")
                        brush_thick = 5
                        activate_voice_command = False
                    elif text == "small" or "small" in text:
                        print("set small brush")
                        brush_thick = 10
                        activate_voice_command = False
                    elif text == "medium" or "medium" in text:
                        print("set medium brush")
                        brush_thick = 20
                        activate_voice_command = False
                    elif text == "big" or "big" in text or "bick" in text or "bic" in text:
                        print("set big brush")
                        brush_thick = 40
                        activate_voice_command = False
                    elif text == "huge" or "huge" in text:
                        print("set huge brush")
                        brush_thick = 60
                        activate_voice_command = False
                    elif text == "giant" or "giant" in text:
                        print("set giant brush")
                        brush_thick = 80
                        activate_voice_command = False
                    elif text == "one" or "one" in text:
                        print("set color slot 1")
                        idk_color = (0, 0, 255)
                        activate_voice_command = False
                    elif text == "two" or text == "too" or "two" in text or "too" in text:
                        print("set color slot 2")
                        idk_color = (0, 0, 255)
                        activate_voice_command = False
                    elif text == "three" or "three" in text or "tee" in text or "tree" in text or "tea" in text:
                        print("set color slot 3")
                        idk_color = (0, 0, 255)
                        activate_voice_command = False
                    elif text == "capture" or "capture" in text:
                        with mss() as sct:
                            sct.shot()
                            print("captured")
                            activate_voice_command = False
                    elif text == "always" or "always" in text:
                        if always_on == False:
                            always_on = True
                        else:
                            always_on = False
                    elif text == "save" or "save" in text or "safe" in text or "sape" in text:
                        print("saving...")
                        all_titles = pygetwindow.getAllTitles()
                        print(all_titles)
                        album = os.listdir("gallery")
                        all_pic = []
                        for each_pic in album:
                            all_pic.append(each_pic)
                        album_empty = False
                        if len(all_pic) <= 0:
                            album_empty = True
                            save_directory = 'gallery/canvas1.png'
                            activate_voice_command = False
                        else:
                            all_int = []
                            for i in range(len(all_pic)):
                                full = all_pic[i]
                                cut_first = full[6:]
                                all_int.append(int(cut_first[:-4]))
                            save_directory = 'gallery/canvas' + str(max(all_int) + 1) + '.png'
                            activate_voice_command = False
                        save_window = pygetwindow.getWindowsWithTitle('Canvas')[0]
                        xx1 = save_window.left
                        yy1 = save_window.top
                        height_1 = save_window.height
                        width_1 = save_window.width
                        xx2 = xx1 + width_1
                        yy2 = yy1 + height_1
                        save_path = 'gallery'
                        pyautogui.screenshot(save_directory)
                        im = Image.open(save_directory)
                        im = im.crop((xx1, yy1, xx2, yy2))
                        im.save(save_directory)

                        print("canvas saved")
                    elif text == "exit" or "exit" in text or "except" in text:
                        print("exiting...")
                        over = True
                        activate_voice_command = False
                    elif text == "show" or "show" in text or "cho" in text or "chow" in text:
                        show_tab = True
                        activate_voice_command = False
                    elif text == "blind" or "blind" in text or "bind" in text:
                        show_tab = False
                        activate_voice_command = False
                    elif text == "nothing" or "nothing" in text:
                        print("do nothing")
                    elif text == "clear" or "clear" in text:
                        print("clear")
                        # x_point,y_point = 0,0
                        cv2.rectangle(black_canvas, (0, 0), (1280, 720), eraser_color, cv2.FILLED, )
                        activate_voice_command = False
                    elif text == "done" or "done" in text or "finish" in text:
                        print("saving...")
                        all_titles = pygetwindow.getAllTitles()
                        print(all_titles)
                        album = os.listdir("gallery")
                        all_pic = []
                        for each_pic in album:
                            all_pic.append(each_pic)
                        album_empty = False
                        if len(all_pic) <= 0:
                            album_empty = True
                            save_directory = 'gallery/canvas1.png'
                            activate_voice_command = False
                        else:
                            all_int = []
                            for i in range(len(all_pic)):
                                full = all_pic[i]
                                cut_first = full[6:]
                                all_int.append(int(cut_first[:-4]))
                            save_directory = 'gallery/canvas' + str(max(all_int) + 1) + '.png'
                            activate_voice_command = False
                        save_window = pygetwindow.getWindowsWithTitle('Canvas')[0]
                        xx1 = save_window.left
                        yy1 = save_window.top
                        height_1 = save_window.height
                        width_1 = save_window.width
                        xx2 = xx1 + width_1
                        yy2 = yy1 + height_1
                        save_path = 'gallery'
                        pyautogui.screenshot(save_directory)
                        im = Image.open(save_directory)
                        im = im.crop((xx1, yy1, xx2, yy2))
                        im.save(save_directory)

                        print("canvas saved")
                        over = True
                        print("leaving")
                        break

                except:
                    print("Sorry, couldn't recognize your voice.")
        if over == True:
            break


t1 = threading.Thread(target=main)
t2 = threading.Thread(target=voice_command)

t1.start()
t2.start()
