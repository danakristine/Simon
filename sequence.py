#imports
import board
import time
from digitalio import DigitalInOut, Direction
import random

# configurations & setup of leds
red = DigitalInOut(board.D2)
red.direction = Direction.OUTPUT
red.value = False


green = DigitalInOut(board.D3)
green.direction = Direction.OUTPUT
green.value = False

yellow = DigitalInOut(board.D4)
yellow.direction = Direction.OUTPUT
yellow.value = False

blue = DigitalInOut(board.D5)
blue.direction = Direction.OUTPUT
blue.value = False

# configurations & setup of buttons
whiteb = DigitalInOut(board.D6)
whiteb.direction = Direction.INPUT


blackb = DigitalInOut(board.D7)
blackb.direction = Direction.INPUT


orangeb = DigitalInOut(board.D8)
orangeb.direction = Direction.INPUT


# creating functions
def add_to_sequence(lyst):
    lyst.append(random.randint(0,3))
    print(lyst)


def display_sequence(jist):
    for item in jist:
        if item == 0:
            red.value = True
            time.sleep(0.3)
            red.value = False
            
        if item == 1:
            green.value = True
            time.sleep(0.3)
            green.value = False
            
        if item == 2:
            yellow.value = True
            time.sleep(0.3)
            yellow.value = False
            
        if item == 3:
            blue.value = True
            time.sleep(0.3)
            blue.value = False
            

# main
mist = []
while True:
    if blackb.value:
        add_to_sequence(mist)
        print("added")
    if whiteb.value:
        display_sequence(mist)
        print(mist)
    if orangeb.value:
        mist = []
    
        
