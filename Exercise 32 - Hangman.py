# -*- coding: utf-8 -*-
"""
G. L. Roberts 

30th September 2017

http://www.practicepython.org/exercise/2017/01/10/32-hangman.html

Complete implementation of hangman
"""

import sys
import random
import requests
import os

def main():
    wordToGuess=getRandWord()
    wordToGuess=wordToGuess.upper() # Uppercase for matching
    playHangman(wordToGuess)
    
def getRandWord():
    """Chooses a random word from sowpods. Please download it first to speed up
    the program"""
    
    if os.path.isfile('./wordList.txt'):
        with open('wordList.txt') as file:
            dataList=file.read().splitlines()
    else:
        data = requests.get('http://norvig.com/ngrams/sowpods.txt')
        dataList=data.text.split('\r\n')
    return dataList[random.randint(0,len(dataList))]

def playHangman(wordToGuess):
    """ Allows a user to play hangman. They guess single letters and if it is in 
    the word, the word is displayed """

    guesses='' # Blank string to store all guesses
    incorrectGuesses=0
    
    print("Welcome to hangman, you have 6 guesses!"+"\n"+"_ "*len(wordToGuess))
    while True:
        guess=guessLetter()
        if guess in guesses:
            print("You've guessed that before!")    
        if guess not in wordToGuess:
            incorrectGuesses+=1
            if incorrectGuesses>=6:
                print("You lost! The word was "+wordToGuess)
                break
            print("Incorrect! You have "+str(6-incorrectGuesses)+" guesses remaining")
            
        else:
            guesses+=guess
            progress=printProgress(wordToGuess,guesses)
            if progress==0:
                print("Congratulations you have won!")
                break

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

