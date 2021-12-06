# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random, sys

def header():
    print ("Lottery")
    print ("Try your luck! Input three unique numbers ranging from 0 to 9 now!")

header ()

_tryagain = 'yup'
while _tryagain [0] == 'y':
    _winningList = []
    for i in range(0,3):
        randomm = random.randint(0,9)
        while randomm in _winningList:
            randomm = random.randint(0,9)
        _winningList.append (randomm)
    _winningList.sort ()

    _inputList = []
    for i in range(0,3):
        _number = int(input(f"#{i+1}: "))
        while _number in _inputList:
            _number = int(input(f"#{i+1}: "))
        _inputList.append (_number)
    _inputList.sort()

    if (_winningList == _inputList):
        print ("Winner!")
    else:
        print ("You loss!")
    print (_winningList)
    print (_inputList)
    _tryagain = input ("Wanna try again? (y or n): ") 
else: sys.exit()