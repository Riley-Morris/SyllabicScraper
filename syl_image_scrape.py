import pyautogui
import time
import os
from PIL import Image

#create directory
syl_folder = 'Raw_syllabics'
if syl_folder not in os.listdir():
    os.mkdir(folder)
#website to have open on fullscreen on chrome with(width=1920, height=1080) resolution
#https://dictionary.eastcree.org/words
list_of_terms = [

    'insect', 'knife' 'axe' 'fire'
]
#iterate over list
for syl in list_of_terms:
    #click search bar
    pyautogui.moveTo(236, 456)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(syl)
    pyautogui.press('enter')
    time.sleep(3)


    #go to first result
    pyautogui.moveTo(172, 669)
    pyautogui.click()
    time.sleep(3)

    #move mouse away
    pyautogui.moveTo(1827, 212)
    time.sleep(10)
    screenshot = pyautogui.screenshot()


    screenshot.save(f"Raw_syllabics\\{syl}.png")


    # get raw images for syllabics
    im = Image.open(f'Raw_syllabics\\{syl}.png')

    left = 188
    top = 741
    right = 700
    bottom = 800

    # crop image
    imcrop = im.crop((left, top, right, bottom))

    # save image
    imcrop.save(f'ImageSyllabics\\{syl}.png')

