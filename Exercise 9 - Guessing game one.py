# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Higher or lower guessing game
"""

import random
import sys

def main():
    randomNumber=random.randint(1,9)
    numberOfGuesses=0
    while True:
        guess=userGuess()
        numberOfGuesses=numberOfGuesses+1
        if guess==randomNumber:
            print("Correct!")
            break
        elif guess>randomNumber:
            print("Too high!")
        elif guess<randomNumber:
            print("Too low!")
    print("You were successful in " + str(numberOfGuesses) + " guesses!")

def userGuess():
    while True:
        try:
            guess=input("Guess the number (or type 'exit' to leave): ")
            if guess.lower()=='exit':
                sys.exit("You asked to leave")
            else:
                guess=int(guess)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if guess>10 or guess<1:
            print("Guess between 1 and 9 please\n")
            continue
        else:
            break
    return guess
        
if __name__ == "__main__":
    main()

