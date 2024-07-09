import pyautogui
import time

#O desafio é tocar um MP3, mais eu quero tomar uma música no Youtube.

pyautogui.press('win')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.write('https://www.youtube.com')
time.sleep(2)
pyautogui.press('enter')