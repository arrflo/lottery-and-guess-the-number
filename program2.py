# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

def header ():
    print ("Guess the Number!")

def getRaandom ():
    randomm = random.randint(0,100)
    return randomm

header ()
number = getRaandom ()
userNumber = int (input ("Ranging from 0-100, which number do you think is it?: "))

while userNumber != number:
    if userNumber > number:
        print ("Greater than")
    elif userNumber < number:
        print ("Less than")
    userNumber = int (input ("Ranging from 0-100, which number do you think is it?: "))
    userNumber == number
else: print ("You nailed it!")

