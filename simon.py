# imports
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

redb = DigitalInOut(board.D7)
redb.direction = Direction.INPUT

greenb = DigitalInOut(board.D8)
greenb.direction = Direction.INPUT

yellowb = DigitalInOut(board.D9)
yellowb.direction = Direction.INPUT

blueb = DigitalInOut(board.D10)
blueb.direction = Direction.INPUT

# extra variables
start = False
points = 0
user_press = 1
user_idx = 0
game = False

# creating functions
def add_to_sequence(lyst):
    lyst.append(random.randint(0, 3))
    print(lyst)


def display_sequence(jist):
    for item in jist:
        if item == 0:
            red.value = True
            time.sleep(0.3)
            red.value = False
            time.sleep(0.3)

        if item == 1:
            green.value = True
            time.sleep(0.3)
            green.value = False
            time.sleep(0.3)

        if item == 2:
            yellow.value = True
            time.sleep(0.3)
            yellow.value = False
            time.sleep(0.3)

        if item == 3:
            blue.value = True
            time.sleep(0.3)
            blue.value = False
            time.sleep(0.3)


# def game_over:


def display_scr():
    print(points)
    blue.value = True
    red.value = True
    yellow.value = True
    green.value = True
    time.sleep(0.2)
    blue.value = False
    red.value = False
    yellow.value = False
    green.value = False
    time.sleep(0.2)


def reset():
    global start
    global mist
    start = False
    mist = []


def user_updated():
    global user_press
    user_press = -1
    if redb.value:
        red.value = True
        time.sleep(0.3)
        red.value = False
        time.sleep(0.3)
        user_press = 0
        print("user:")
        print(user_press)

    if greenb.value:
        green.value = True
        time.sleep(0.3)
        green.value = False
        time.sleep(0.3)
        user_press = 1
        print("user:")
        print(user_press)

    if yellowb.value:
        yellow.value = True
        time.sleep(0.3)
        yellow.value = False
        time.sleep(0.3)
        user_press = 2
        print("user:")
        print(user_press)

    if blueb.value:
        blue.value = True
        time.sleep(0.3)
        blue.value = False
        time.sleep(0.3)
        user_press = 3
        print("user:")
        print(user_press)


def comparing_led():
    global game
    global user_idx, user_press
    while not (blueb.value or redb.value or yellowb.value or greenb.value):
        pass
    if blueb.value or redb.value or yellowb.value or greenb.value:
        user_updated()
        for i in range(len(mist)):
            if mist[user_idx] == user_press:
                user_idx += 1
                user_updated()
                add_to_sequence(mist)
                display_sequence(mist)
            else:
                display_scr()
                #reset()
                #game = False
    game = True


# main
mist = []

while True:
    if not start and whiteb.value:
        start = True
        time.sleep(0.5)
        if start:
            add_to_sequence(mist)
            display_sequence(mist)
            game = comparing_led()
            if game:
                score += 1
                time.sleep(1.0)



















