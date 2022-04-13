import cv2
import numpy as np
from pyautogui import *
import time
import random
import win32api, win32con
from win32api import GetSystemMetrics
import keyboard
from pynput.keyboard import Key, Controller
# LIST OF TASKS
'''
1. Wires
2. 1234..
3. Steering
4. Divert
5. Trash
'''
map = input("Which Map? ")
keyboard = Controller()

while 1:
    if locateOnScreen('Images/Wires.png', confidence = 0.9, region = (1000,425,60,60)) != None:
        im1 = screenshot(region = (510,253,120,600))
        im1.save(r"C:\Users\dimer\Desktop\Among Us Bot\Images\left_wires.png")
        im2 = screenshot(region = (1250,270,170,610))
        im2.save(r"C:\Users\dimer\Desktop\Among Us Bot\Images\right_wires.png")
        colour_list = ["red","blue","yellow","pink"]
        multipliers = [0,1,2,3]
        for i in range(0,4):
            if len(multipliers) == 1:
                    movex = 85
                    movey = multipliers[0]*190
                    moveTo(515,253+15 + i*190)
                    mouseDown()
                    moveTo(1250+movex,270 + movey)
                    mouseUp()
                    multipliers.pop(0)
            else:
                colour_to_match = im1.getpixel((5,15 + i*190))
                for j in multipliers:
                    if im2.getpixel((85,j*185)) == colour_to_match:
                        movex = 85
                        movey = j*190
                        moveTo(515,253+15 + i*190)
                        mouseDown()
                        moveTo(1250+movex,270 + movey)
                        mouseUp()
                        multipliers.remove(j)
                        break
        sleep(2.0)
    if locateOnScreen('Images/manifolds.png',confidence = 0.8, region = (1000,425,60,60)) != None:
        start = time.perf_counter()
        for i in range(1,11):
            click(locateOnScreen(f'Images/{i}.png', confidence = 0.8, region = (600,425,750,270)))
    if locateOnScreen('Images/steering.png',confidence = 0.9, region = (1000,100,20,20)) != None:
        moveTo(GetSystemMetrics(0)/2,GetSystemMetrics(1)/2)
        mouseDown()
        mouseUp()
    if locateOnScreen('Images/divert.png', confidence = 0.9, region = (1000,100,60,60)) != None:
        moveTo(locateOnScreen('Images/power_switch.png', confidence = 0.9))
        mouseDown()
        move(0,-100)
        mouseUp()
    if locateOnScreen('Images/rotateDivert.png', confidence =0.9, region = (1000,500,60,60)) != None:
        moveTo(GetSystemMetrics(0)/2,GetSystemMetrics(1)/2)
        mouseDown()
        mouseUp()
    if locateOnScreen('Images/trash_lever.png', confidence = 0.9) != None:
        moveTo(locateOnScreen('Images/trash_lever.png', confidence = 0.9))
        mouseDown()
        move(0,500)
        sleep(1.4)
        mouseUp()