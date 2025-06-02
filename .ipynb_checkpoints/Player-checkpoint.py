from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import time

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

def test():
    time.sleep(2)
    keyboard.type(" Flats")
    keyboard.press(Key.left)
    keyboard.release(Key.left)
test()
