# import
import random


# creating function
def add_to_sequence(lyst):
    lyst.append(random.randint(0,3))
    print(lyst)


def display_sequence(jist):
    for item in jist:
        if item == 0:
            print("Red")
        if item == 1:
            print("Green")
        if item == 2:
            print("Yellow")
        if item == 3:
            print("Blue")

# main
list = []
while True:
    print("1. Add to Sequence")
    print("2. Display Sequence")
    print("3. Exit Program")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_to_sequence(list)
    if choice == "2":
        display_sequence(list)
    if choice == "3":
        break
