import cv2 as cv
import numpy as np
import pyautogui
import time
import random
import win32api, win32con

pyautogui.sleep(1)
im1 = pyautogui.screenshot(region = (1000,500,60,60))
im1.save(r"C:\Users\dimer\Desktop\Among Us Bot\Images\rotateDivert.png")