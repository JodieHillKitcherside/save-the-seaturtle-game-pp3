import sys
import time
import pygame


def main():
    # Run all program functions 
    # textPrint(text)
    introScene()
    oaxacaBeach()
    gillnetRescue()
    tangledExit()
    swimWithFriends()
    exit()


""" def text_print(text):
    # Format the text type effect on users screen
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')"""


# Constant with a list of options for user/ player 
# Import pygame.locals for access to key coordinates 
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT, 
    K_ESCAPE,
    QUIT,
)

pygame.init()

running = True

while running:
    for event in pygame.event.get():
        if event.type == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False 


# Customise exception class for wrong key pressed
class wrongKey(KeyError):
    pass


if __name__ == "__main__":
    # Print introductory text,
    # Ask user to input name 
    # Start introScene function
    # Text instructions 

    # text = "Save the Sea Turtle Game"

    print("Welcome to the Save the Sea Turtle Game!")
    print("Ahoy! As an endagered seaturtle, you are peacefully riding") 
    print("the Pacific Ocean. We are going to take you on a mini adventure,") 
    print("watch out for the Great White shark, and be aware of")
    print("other terrors.")
    print("First, let's start with your name!")
    name = input("Please enter your name:")
    print(name + ", great. Now you have 4 directions to choose from.")
    print("Which way will you go next?")
    print("Options(Key) - Up, down, Left, Right")


def exit(main):
    print("Well done on getting that far. I'm sure you've worked out by now") 
    print("that unfortunately sea turtles face many threats to their survival")
    print("and although some are natural - most are human threats.")
    print("If you survived, you're made of strong stuff. It's estimated that")
    print("only 1 in 1000 sea turtles make it to adult turtle.")
    introScene()


def oaxacaBeach():
    # Present option for right "arriving at Oaxaca Beach"
    # Set function for vulturesLurk with options to select
    # Call functions for babiesSafe and fleeExit
    print("Wow mama! You have many eggs to lay, you've ended up swimming")
    print("to Oaxaca Beach! Lets see if you can protect them all!")

    def vultureLurk():
        print("Watch out! Vultures are out to attact!")
        print(name + "Select your next option: Up or Right!")
        userInput = input()
        if userInput == "K_UP":
            fleeExit()
        elif userInput == "K_RIGHT":
            babiesSafe()
        else:
            print("Please enter valid key option for the")
            print("Save the Sea Turtle Game.")


def babiesSafe(exit):
    print("Phew! You dug a deep nest and all the babies are safe!")
    print("You tried so hard in the heat and wading through the thick sand.")
    print("Amazing, you have 100 baby turtle eggs protected!")
    exit()


def fleeExit(exit):
    print("Vultures visciously circled and you fled back to the ocean!")
    print("You're so lucky! You made it back to ride the tide!")
    print("You can try again tomorrow.")
    exit()


def gillnetRescue():
    # Present option for up "being caputred by gillnets"
    # Set function for rescueExit 
    # Call function for rescueExit 

    def rescueExit(exit):
        print("Yay! The rescue team are taking you to rehab, looks like your")
        print("injuries will be fixed and you are going back")
        print("to the open ocean!")
        exit()

    print("Oh! Unfortunatley you have been accidentally captured by gillnets!")
    print("Fishermen are so sorry and have called ocean rescue!")
    
    rescueExit()   


def tangledExit(exit):
    # Present option for down "bad storms mean you're tangled"
    # Call function for Exit 
    print("Bad storms mean that fishermens nets are no longer drying")
    print("on the beach and made it in to the water!")
    print(" oops, you got tangled. You are on your")
    print("own in the deep ocean and nobody can help this time! :(")
    exit()


def swimWithFriends():
    # Present option for left "still peacefully swimming"
    
    def greatWhite():
        def sharkBaitExit(exit):
            print("He got you! You tried to get away but he's too fast.") 
            print("You're dead.")
            exit()

        def freedomExit(exit):
            print("You swam up and out of sight! You are free.")
            exit()

        print("Can you hide from the great white shark? He's spotted you!")
        print(name + "Select your next option: Up or Left!")
        userInput = input()
        if userInput == "Up":
            sharkBaitExit()
        elif userInput == "Left":
            freedomExit()
        else:
            print("Please enter valid key option for the")
            print("Save the Sea Turtle Game.")

    greatWhite()


def introScene():
    # Add options for directions the user/ player can choose from
    # Ask user to select key
    directions = ["down", "up", "left", "right"]
    print(name + ", great. Now you have 4 directions to choose from.")
    print("Which way will you go next?")
    userInput = ""
    while userInput not in directions:
        print(name + "your options: (key in) - Up/ Down/ Left/ Right")
        userInput = input()
        if userInput == "K-UP":
            gillnetRescue()
        elif userInput == "K_DOWN":
            tangledExit()
        elif userInput == "K_LEFT":
            oaxacaBeach()
        elif userInput == "K_RIGHT":
            swimWithFriends()
        else:
            print("Please enter valid key option for the")
            print("Save the Sea Turtle Game.")


main() 