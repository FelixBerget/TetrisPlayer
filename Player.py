from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import time
from PIL import Image, ImageGrab
from tkinter import *
from tkinter.ttk import *


screenInfo = Tk()
screenHeight = screenInfo.winfo_screenheight()
screenWidth = screenInfo.winfo_screenwidth()
keepTrying = True
#Testing command inputs
keyboard = KeyboardController()

#Commands to control the inputs
def turnLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def turnRight():
    keyboard.press(Key.right)
    keyboard.release(Key.rigth)

def turnDown():
    keyboard.press(Key.down)
    keyboard.release(Key.down)



#Test for playing constantly
while keepTrying:
    time.sleep(10)
    print(screenHeight)
    print(screenWidth)
    screenshot = ImageGrab.grab(bbox =(screenWidth/4,screenHeight/5,screenWidth/1.7,screenHeight)) 
    screenshot.show()
    print("tatt screenshot")
    
    

