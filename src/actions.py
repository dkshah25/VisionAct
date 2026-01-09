import pyautogui
import random
import time

def click_human_like(x, y, delay):

    pyautogui.moveTo(x, y, duration=0.15)
    time.sleep(delay)
    pyautogui.click()