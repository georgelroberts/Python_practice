# -*- coding: utf-8 -*-
"""
G. L. Roberts 

27th September 2017

http://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

Continuing with the hangman game, this allows the user to guess letters in
the word
"""

import sys

def main():
    wordToGuess='evaporate'
    wordToGuess=wordToGuess.upper() # Uppercase for matching
    playHangman(wordToGuess)

def playHangman(wordToGuess):
    """ Allows a user to play hangman. They guess single letters and if it is in 
    the word, the word is displayed """

    guesses='' # Blank string to store all guesses
    incorrectGuesses=0
    
    print("Welcome to hangman"+"\n"+"_ "*len(wordToGuess))
    while True:
        guess=guessLetter()
        if guess in guesses:
            print("You've guessed that before!")    
        if guess not in wordToGuess:
            print("Incorrect! ")
            incorrectGuesses+=1
        else:
            guesses+=guess
            progress=printProgress(wordToGuess,guesses)
            if progress==0:
                print("Congratulations you have won!")
                break
            else:
                #print(progress) # Number of incorrect guesses
                continue

def guessLetter():
    """ Gets user input and makes sure it is valid"""
    while True:
        try:
            if sys.version_info[0] < 3:
                guess=raw_input("Please enter a letter: ")
            else:
                guess=input("Please enter a letter: ")
        except ValueError:
        	print("Please enter a valid letter")
        	continue
        if len(guess)!=1 or not guess.isalpha():
        	print("Please make sure you input a single letter")
        	continue
        else:
        	break
        
    return guess.upper()

def printProgress(wordToGuess,guesses):
    """ Prints the word with underscores denoting an unguessed letter """
    revealed=("_ ,"*len(wordToGuess)).split(",")[:-1]
    incorrectGuesses=0
    
    for char in guesses:
        position=-1 #Initialise variable for finding matching characters in the word
        if char in wordToGuess:
            while True:
                position=wordToGuess.find(char,position+1)
                if position>=0:
                    revealed[position]=char+" "
                else:
                    break
            
    print("".join(revealed))
    
    if "_ " not in revealed:
        return 0
    else:
        return 1
        
            
    


if __name__ == "__main__":
    main()

