import pyautogui
import time

time.sleep(0.5)

f = open("./spamlar.txt", "r", encoding="utf-8")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

