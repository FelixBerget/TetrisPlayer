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

#Scores for each figure, and for each side.
iLeftScore = 2
iRightScore = 2
jLeftScore = 2
jRightScore = 2
lLeftScore = 2
lRightScore = 2
oLeftScore = 2
oRightScore = 2
sLeftScore = 2
sRightScore = 2
tLeftScore = 2
tRightScore = 2
zLeftScore = 2
zRightScore = 2


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

previousScore="0"
#Commands to control the inputs
def turnLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def turnRight():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def rotateRight():
    keyboard.press(Key.Up)
    keyboard.relase(Key.Up)

def rotateLeft():
    keyboard.press("z")
    keyboard.release("z")

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
        previousScore = "0"
        return "GAME_OVER"
    return "STILL_PLAYING"
        



#Test for playing constantly and using screenshots
time.sleep(5)
while keepTrying:
    time.sleep(0.5)
    screenshot = ImageGrab.grab(bbox =(450,217,1450,964)).load()
    screenshotTwo = ImageGrab.grab(bbox =(450,217,1450,964))
    scoreboard = ImageGrab.grab(bbox = (560,694,708,728))
    print(screenshot[458,66])
    testTuple = (15,15,15)
    isItGameOver = ""
    isItGameOver = isGameOver()
    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nO figure :")
        for x in range (7):
            rightScore = -oRightScore
            theNumber = random.randint(rightScore, oLeftScore)
            if theNumber < 0 :
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
                    
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        sendDown()
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        print("O figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            oRightScore = oRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                oRightScore = oRightScore / 2
        if moreLeftOrRight > 0:
            oLeftScore = oLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                oLeftScore = oLeftScore / 2
        print ("!O SCORES!")
        print (oRightScore)
        print (oLeftScore)
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[545,96]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nI figure :")
        for x in range (7):
            rightScore = -iRightScore
            theNumber = random.randint(rightScore, iLeftScore)
            if theNumber < 0:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        sendDown()
        print("I figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            iRightScore = iRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                iRightScore = iRightScore / 2
        if moreLeftOrRight > 0:
            iLeftScore = iLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                iLeftScore = iLeftScore / 2
        print ("!I SCORES!")
        print (iRightScore)
        print (iLeftScore)
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[458,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = str(random.randrange(1,10000000))
        imageNumberTwo = str(random.randrange(1,1000))
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nJ figure :")
        for x in range (7):
            rightScore = -oRightScore
            theNumber = random.randint(rightScore, oLeftScore)
            if theNumber < 0:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        sendDown()
        print("J figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            jRightScore = jRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                jRightScore = jRightScore / 2
        if moreLeftOrRight > 0:
            jLeftScore = jLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                jLeftScore = jLeftScore / 2
        print ("!J SCORES!")
        print (jRightScore)
        print (jLeftScore)
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nL figure :")
        for x in range (7):
            rightScore = -oRightScore
            theNumber = random.randint(rightScore, oLeftScore)
            if theNumber < 0:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        sendDown()
        print("L figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            lRightScore = lRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                lRightScore = lRightScore / 2
        if moreLeftOrRight > 0:
            lLeftScore = lLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                lLeftScore = lLeftScore / 2
        print ("!L SCORES!")
        print (lRightScore)
        print (lLeftScore)
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[518,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nS figure :")
        for x in range (7):
            rightScore = -oRightScore
            theNumber = random.randint(rightScore, oLeftScore)
            if theNumber < 0:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        sendDown()
        print("S figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            sRightScore = sRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                sRightScore = sRightScore / 2
        if moreLeftOrRight > 0:
            sLeftScore = sLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                sLeftScore = sLeftScore / 2
        print ("!S SCORES!")
        print (sRightScore)
        print (sLeftScore)
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[458,66]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nZ figure :")
        for x in range (7):
            rightScore = -oRightScore
            theNumber = random.randint(rightScore, oLeftScore)
            if theNumber < 0:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        sendDown()
        print("Z figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            zRightScore = zRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                zRightScore = zRightScore / 2
        if moreLeftOrRight > 0:
            zLeftScore = zLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                zLeftScore = zLeftScore / 2
        print ("!Z SCORES!")
        print (zRightScore)
        print (zLeftScore)
        previousScore=score
        time.sleep(2)

    if isNotBlack(testTuple,screenshot[485,66]) and isNotBlack(testTuple,screenshot[455,96]) and isNotBlack(testTuple,screenshot[519,96]) and isNotBlack(testTuple,screenshot[486,96]):
        pytesseract.tesseract_cmd = path_to_tesseract
        imageNumber = random.randrange(1,10000000)
        imageNumberTwo = random.randrange(1,1000)
        moreLeftOrRight = 0
        with open("Results.txt","a") as f:
            f.write("\nZ figure :")
        for x in range (7):
            rightScore = -oRightScore
            theNumber = random.randint(rightScore, oLeftScore)
            if theNumber < 0:
                turnRight()
                with open("Results.txt","a") as f:
                    f.write("(Right")
                    moreLeftOrRight = moreLeftOrRight - 1
            if theNumber > 0:
                turnLeft()
                with open("Results.txt","a") as f:
                    f.write("(Left")
                    moreLeftOrRight = moreLeftOrRight + 1
        screenshotTwo.save(f"Images/image nr {imageNumber}{imageNumberTwo}.jpg" )
        with open("Results.txt","a") as f:
            f.write(f"[image nr {imageNumber}{imageNumberTwo}.jpg")
        score = pytesseract.image_to_string(scoreboard)
        print(score)
        if score == "":
            score = previousScore
        with open("Results.txt","a") as f:
            f.write(f";score={score}")
        print(score)
        with open("Results.txt","a") as f:
            f.write(f"*{isItGameOver}")
        sendDown()
        print("T figure")
        numScore = int(score)
        numPrevScore = int(previousScore)
        if moreLeftOrRight < 0:
            tRightScore = tRightScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                tRightScore = tRightScore / 2
        if moreLeftOrRight > 0:
            tLeftScore = tLeftScore + numScore - numPrevScore
            if isItGameOver == "GAME_OVER":
                tLeftScore = tLeftScore / 2
        print ("!T SCORES!")
        print (tRightScore)
        print (tLeftScore)
        previousScore=score
        time.sleep(2)
        
    
    

