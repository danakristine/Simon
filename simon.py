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
game = []

# creating functions!!

def add_to_sequence(lyst):
    """
    adds a random number bettwen 0-3 to the game list.

    parameter:
      lyst (list): the name of the list the random int will be added to

    output:
      prints out the list
      
    """
    lyst.append(random.randint(0, 3))
    print(lyst)


def display_sequence(jist):
    """
    lights up the led associated with the random int in the game list
        
    parameter:
       jist (list): the name of the list that is being iterated through
       
    """
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


def game_over():
    """
    lights up each led and sets the game sequence to empty

    takes no args
    
    """
    global game
    blue.value = True
    green.value = True
    red.value = True
    yellow.value = True
    time.sleep(0.3)
    game = []
    blue.value = False
    green.value = False
    red.value = False
    yellow.value = False
    game_start = False
    time.sleep(0.3)
    display_scr(points)
    print(points)



def display_scr(users):
    """
    displays the value of the score
    
    parameter:
    users (int): the number of points

    """
    print(users)


def reset():
    global start
    global game
    start = False
    game = []


def user_updated():
    global user_press
    user_press = -1
    while not (blueb.value or redb.value or yellowb.value or greenb.value):
        pass
        if redb.value:
            red.value = True
            time.sleep(0.3)
            red.value = False
            time.sleep(0.3)
            return 0

        if greenb.value:
            green.value = True
            time.sleep(0.3)
            green.value = False
            time.sleep(0.3)
            return 1

        if yellowb.value:
            yellow.value = True
            time.sleep(0.3)
            yellow.value = False
            time.sleep(0.3)
            return 2

        if blueb.value:
            blue.value = True
            time.sleep(0.3)
            blue.value = False
            time.sleep(0.3)
            return 3


def comparing_led():
    global game
    global user_idx, user_press
    while not (blueb.value or redb.value or yellowb.value or greenb.value):
        pass
    user_press = user_updated()
    for i in range(len(game)):
        if game[user_idx] == user_press:
            user_idx += 1
        else:
            print("wrong!!!")
            user_idx = 0
            game_over()
        
    
def user_seq():
    global user_idx
    global game
    return (user_idx == len(game))




# main

while True:
    if not start and whiteb.value:
        start = True
        time.sleep(0.5)
        if start:
            add_to_sequence(game)
            display_sequence(game)
            comparing_led()
            if user_seq():
                points += 1
                time.sleep(1.0)



















