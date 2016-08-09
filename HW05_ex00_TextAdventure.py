#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0):
    print(name + " walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print( name + 'takes the stairs')
        if (count > 0):
            print("but" + name + " is not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == "run":
    	print(name + " runs away")
    	quit()
        


def gold_room():
    print("This room is full of gold.  How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is " + name  + " going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take"  or next == "honey":
            dead("The bear looks at " + name + " then slaps " + name  +"'s face off.")
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. " + name +" can go through it now.")
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at " + name +" and " + name +" goes insane.")
    print("Does " + name +" flee for his life or eat his head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    global name
    name = str(input("Enter your name "))
    print(name + " is in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
