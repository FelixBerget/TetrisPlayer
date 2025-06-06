from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import time
from PIL import Image, ImageGrab

#This is what reads the score
#The Reward that will be given based on all the choices the model has made
currentReward = 0
#Gets all the info about the screen
keepTrying = True
#Keeps track of the current decsisions such as having gone left
currnetDecision = []
#Testing command inputs
keyboard = KeyboardController()
figures = ["I","J","L","O","S","T","Z"]
#J has the line up on the left side while L has on the right
#S is up on the right side while Z is up on the left side


#under here are all the boxes on the boards bositions x first then y
firstBox = [458,66]
secondBox = [485,66]
thirdBox = [518,66]
fourthBox = [551,66]

anotherFirstBox = [455,96]
anotherSecondBox = [486,96]
anotherThirdbox = [519,96]
anotherFourthBox = [545,96]

#Commands to control the inputs
def turnLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def turnRight():
    keyboard.press(Key.right)
    keyboard.release(Key.rigth)

def sendDown():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def isNotBlack(testTuple, currentSpot):
    isNotBlack = False
    if testTuple[0] < currentSpot[0] or testTuple[1] < currentSpot[1] or testTuple[2] < currentSpot[2]:
        isNotBlack = True
    print(isNotBlack)
    return isNotBlack



#Test for playing constantly and using screenshots
time.sleep(5)
while keepTrying:
    time.sleep(0.5)
    screenshot = ImageGrab.grab(bbox =(450,217,1450,964)).load()
    print(screenshot[458,66])
    testTuple = (15,15,15)
    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        print("O figure")
        time.sleep(10)

    if isNotBlack(testTuple,screenshot[545,96]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        print("I figure")
        time.sleep(10)

    if isNotBlack(testTuple,screenshot[458,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        print("J figure")
        time.sleep(10)

    if isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[486,96]):
        print("L figure")
        time.sleep(10)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[486,96]):
        print("S figure")
        time.sleep(10)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[458,66]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        print("Z figure")
        time.sleep(10)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        print("T figure")
        time.sleep(10)
        
    
    

