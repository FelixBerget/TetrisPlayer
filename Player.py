from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import time
from PIL import Image, ImageGrab
from tkinter import *
from tkinter.ttk import *
from pytesseract import pytesseract

#This is what reads the score
pathTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#The Reward that will be given based on all the choices the model has made
currentReward = 0
#Gets all the info about the screen
screenInfo = Tk()
screenHeight = screenInfo.winfo_screenheight()
screenWidth = screenInfo.winfo_screenwidth()
keepTrying = True
#Keeps track of the current decsisions such as having gone left
currnetDecision = []
#Testing command inputs
keyboard = KeyboardController()
pytesseract.tesseract_cmd = pathTesseract

#Commands to control the inputs
def turnLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def turnRight():
    keyboard.press(Key.right)
    keyboard.release(Key.rigth)

def turnDown():
    keyboard.press(Key.space)
    keyboard.release(Key.space)



#Test for playing constantly and using screenshots
while keepTrying:
    time.sleep(10)
    print(screenHeight)
    print(screenWidth)
    screenshot = ImageGrab.grab(bbox =(screenWidth/4,screenHeight/5,screenWidth/1.7,screenHeight)) 
    screenshotText = pytesseract.image_to_string(screenshot)
    print(screenshotText)
    screenshot.show()
    print("tatt screenshot")
    
    

