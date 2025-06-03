from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import time


#Testing command inputs
keyboard = KeyboardController()
time.sleep(3)

keyboard.press(Key.shift)
keyboard.press('j')
keyboard.release('j')
time.sleep(2)
keyboard.release(Key.shift)
keyboard.press('o')
keyboard.release('o')
time.sleep(2)
keyboard.press('h')
keyboard.release('h')
time.sleep(2)
keyboard.press('n')
keyboard.release('n')

keepTrying = True

def test():
    time.sleep(2)
    keyboard.type(" Flats")
    keyboard.press(Key.left)
    keyboard.release(Key.left)
test()

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

def turnUp():
    keyboard.press(Key.up)
    keyboard.release(Key.up)



#Test for playing constantly
while keepTrying:
    time.sleep(3)
    print("Player Player")
    

