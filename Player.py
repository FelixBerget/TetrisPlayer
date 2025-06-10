from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import time
from PIL import Image, ImageGrab
import PIL
import random
from pytesseract import pytesseract

#This is what reads the score
#The Reward that will be given based on all the choices the model has made
currentReward = 0
#Gets all the info about the screen
keepTrying = True
#Keeps track of the current decsisions such as having gone left
currnetDecision = []
#Testing command inputs
keyboard = KeyboardController()
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
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

gameOverTopCorner = [849,412]
gameOverBottomCorner = [1083,469]

randomDecision = [1,2]

previousScore="0"
#Commands to control the inputs
def turnLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def turnRight():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def sendDown():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def isNotBlack(testTuple, currentSpot):
    isNotBlack = False
    if testTuple[0] < currentSpot[0] or testTuple[1] < currentSpot[1] or testTuple[2] < currentSpot[2]:
        isNotBlack = True
    return isNotBlack

def isGameOver():
    gameoverScreenshot = ImageGrab.grab(bbox = (849,412,1083,469))
    pytesseract.tesseract_cmd = path_to_tesseract
    textOver = pytesseract.image_to_string(gameoverScreenshot)
    print(textOver)
    if "GAME OVER" in textOver:
        print("DOIN IT")
        



#Test for playing constantly and using screenshots
time.sleep(5)
while keepTrying:
    time.sleep(0.5)
    screenshot = ImageGrab.grab(bbox =(450,217,1450,964)).load()
    screenshotTwo = ImageGrab.grab(bbox =(450,217,1450,964))
    scoreboard = ImageGrab.grab(bbox = (560,694,708,728))
    print(screenshot[458,66])
    testTuple = (15,15,15)
    isGameOver()
    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        with open("Results.txt","a") as f:
            f.write("\nFigure is a O figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        sendDown()
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        print("O figure")
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[545,96]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        with open("Results.txt","a") as f:
            f.write("\nFigure is a I figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        sendDown()
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        print("I figure")
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[458,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = str(random.randrange(1,10000000))
        imageNumberTwo = str(random.randrange(1,1000))
        with open("Results.txt","a") as f:
            f.write("\nFigure is a J figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        sendDown()
        print("J figure")
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        with open("Results.txt","a") as f:
            f.write("\nFigure is a L figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        sendDown()
        print("L figure")
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        with open("Results.txt","a") as f:
            f.write("\nFigure is a S figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        sendDown()
        print("S figure")
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[458,66]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        with open("Results.txt","a") as f:
            f.write("\nFigure is a Z figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        sendDown()
        print("Z figure")
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        with open("Results.txt","a") as f:
            f.write("\nFigure is a Z figure :")
        for x in range (7):
            theNumber = random.choice(randomDecision)
            if theNumber == 1:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Turning Right)")
            if theNumber == 2:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Turning Left)")
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg]")
        score = pytesseract.image_to_string(scoreboard)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        sendDown()
        print("T figure")
        previousScore=score
        time.sleep(2)
        
    
    

