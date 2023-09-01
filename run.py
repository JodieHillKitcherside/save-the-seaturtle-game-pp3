from statements import (
    beachPartyExitPrint,
    fleeExitPrint,
    rescueExitPrint,
    tangledExitPrint,
    sharkBaitExitPrint,
    balloonExitPrint,
    vesselStrikeExitPrint,
    babiesSafePrint
)
import sys
import time
import keyboard
import pyfiglet
from emojis import Emoji


def slowprint(all_strings):
    # Styling all strings with a delayed type time
    for each_character in all_strings + "\n":
        sys.stdout.write(each_character)
        sys.stdout.flush()
        time.sleep(1/17)


event = keyboard.read_event()  # Capture a keyboard event


def escape():
    # Implementing a hotkey
    if event.name == 'esc':
        return main()
    else:
        None


def check_user_input(input_str):
    # Validates all user input
    # Prints prompt if blank
    if event.name == "":
        print("Please enter your input")
    else:
        None


# Use pyfiglet module
result = pyfiglet.figlet_format("Save the Sea Turtle", font="digital")
print(result)


# Rename Emoji class
emoji_choice = Emoji()


def main():
    # Introduce main start screen
    introScene()


def exit():
    # Exit function exits the game
    slowprint(
        "GAME OVER" + name + emoji_choice.skull +
        "Well done on getting that far. I'm sure you've worked out by now" +
        "that unfortunately sea turtles face many threats to their survival" +
        "and although some are natural - most are human threats." +
        emoji_choice.pirateflag +
        "If you survived, you're made of strong stuff. It's estimated that" +
        "only 1 in 1000 sea turtles make it to adult turtle."
        + emoji_choice.seaturtle)
    sys.exit()


def slowPrintExit(all_strings):
    # Reusable function to exit game
    # Links to print_statements
    slowprint(all_strings)
    exit()


def oaxacaBeach():
    # Offer user right or down keys to continue game
    # Based on right, proceed to vultureLurk
    # Based on down, proceed to disoriented
    slowprint(
        "Wow mama! You have many eggs to lay, you've" +
        "ended up swimming"
        + emoji_choice.egg
        + "to Oaxaca Beach! Lets see if you can protect"
        + "them all!" + emoji_choice.mexico
        + " Select your next option:"
        + " Choose either 'l'" + emoji_choice.e_left
        + " or choose 'd'" + emoji_choice.e_down)
    if event.name == 'l':
        vultureLurk()
    elif event.name == 'd':
        disoriented()
    else:
        print(KeyError + "Please enter a valid key option.")


def vultureLurk():
    # Offer user up or right keys to continue game
    # Based on up, proceed to fleeExit
    # Based on right, proceed to babiesSafe
    slowprint(
        "Watch out! Vultures are out to attack!" +
        emoji_choice.vulture
        + name + ", select your next option:"
        + " Choose either 'u'" + emoji_choice.e_up
        + " or choose 'r'" + emoji_choice.e_right)
    if event.name == 'u':
        fleeExit()
    elif event.name == 'r':
        babiesSafe()
    else:
        print(KeyError + "Please enter a valid key option.")
    vultureLurk()


def babiesSafe():
    # Exit game
    slowPrintExit(babiesSafePrint)


def fleeExit():
    # Exit game
    slowPrintExit(fleeExitPrint)


def disoriented():
    # Continue to beachPartExit
    slowprint(
        "You seem a bit disorientated! Humans like to surf here and"
        + emoji_choice.divingmask
        + "this means the beach has changed so much since you were"
        + emoji_choice.compass
        + "first here, 20 years ago. Will you find a quiet place"
        "to protect your eggs?")
    beachPartyExit()


def beachPartyExit():
    # Exit game
    slowPrintExit(beachPartyExit)


def gillnetRescue():
    # Continue to rescueExit
    slowprint(
        "Oh! Unfortunately, you have been accidentally captured!"
        + emoji_choice.motorboat
        + "You are stuck in gillnets and struggling to get out"
        + emoji_choice.buoy
        + "means you have deep cuts on your flippers..."
        + "Fishermen are so sorry and have called ocean rescue!")
    rescueExit()


def rescueExit():
    # Exit game
    slowPrintExit(rescueExitPrint)


def tangledExit():
    # Exit game
    slowPrintExit(tangledExitPrint)


def swimWithFriends():
    # Offer user up or left keys to continue game
    # Based on up, proceed to greatWhite
    # Based on left, proceed to oilSpill
    slowprint(
        "Looks like you've found some friends! you are swimming around"
        + emoji_choice.jellyfish
        + "kelp, little fishes and terrible claw lobsters."
        + emoji_choice.lobster
        + "Woah!There is lots of food here!"
        + emoji_choice.crab
        + "Which way will you go?"
        + " Enter your option: 'u'" + emoji_choice.e_up
        + " or 'l'" + emoji_choice.e_left)
    if event.name == 'u':
        greatWhite()
    elif event.name == 'l;':
        oilSpill()
    else:
        print(KeyError + "Please enter a valid key option.")


def greatWhite():
    # Offer user up or left keys to continue game
    # Based on up, proceed to sharkBaitExit
    # Based on left, proceed to balloonExit
    slowprint(
        "Can you hide from the great white shark? He's spotted you!"
        + emoji_choice.shark
        + name
        + ", select your next option: 'u'" + emoji_choice.e_up
        + " or 'l'" + emoji_choice.e_left)
    if event.key == 'u':
        sharkBaitExit()
    elif event.key == 'l':
        balloonExit()
    else:
        print(KeyError + "Please enter a valid key option.")


def sharkBaitExit():
    # Exit game
    slowPrintExit(sharkBaitExitPrint)


def balloonExit():
    # Exit game
    slowPrintExit(balloonExitPrint)


def oilSpill():
    # Continue to vesselStrikeExit
    slowprint(
        "There's been an oil spill affecting your favourite"
        + emoji_choice.biohazard
        + "corals! You are going to have to rest by the"
        + emoji_choice.reef
        + "mangroves instead. Take a five minute rest and get"
        + "back to swimming.")
    vesselStrikeExit()


def vesselStrikeExit():
    # Exit game
    slowPrintExit(vesselStrikeExitPrint)


def introScene():
    # Make name recognised as global
    global name
    name = input("Please enter your name: \n")
    slowprint(
        name + ", great. Now you have 4 directions to choose from."
        + " Your options are on your keyboard."
        + " Throughout this adventure, all you need to tap is:"
        + " 'u' button for Up, 'd' button for Down, 'l' button for Left"
        + " or 'r' button for Right"
        + " And if you would like to escape anytime - hit escape!"
        + " Which way will you go next?"
        + " Enter key")
    if event.name == 'u':
        gillnetRescue()
    elif event.name == 'd':
        tangledExit()
    elif event.name == 'l':
        oaxacaBeach()
    elif event.name == 'r':
        swimWithFriends()
    else:
        print(
            KeyError + "Please enter a valid key option"
            + "(u/d/l/r)")


if __name__ == "__main__":
    slowprint(
        "Welcome to the Save the Sea Turtle Game!"
        # ... [introductory text]
        + " Ahoy! As an endangered sea turtle, you are peacefully riding"
        + emoji_choice.whale
        + "the Pacific Ocean. We are going to take you on an adventure!"
        + emoji_choice.dolphin
        + "Watch out for the Great White Shark and other great terrors."
        + emoji_choice.okay)
    main()
