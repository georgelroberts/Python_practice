# -*- coding: utf-8 -*-
"""
G. L. Roberts 

16th August 2017

http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

Create a game of cows and bulls. A four digit number is generated. The user 
makes a guess and is told how many numbers are in the correct place (bulls) and
how many are in the incorrect place (cows).
EDIT: The digits must be unique, as in the original game.
"""
import random
import sys
import string

def main():
    num2Guess=''.join(random.sample(string.digits,4))
    print(num2Guess)
    
    while True:
        guess=guessNumber()
        cows=0
        bulls=0
        
        for i in range(4):
            if guess[i]==num2Guess[i]:
                bulls=bulls+1
            elif guess[i] in num2Guess:
                cows=cows+1
                
        if bulls==4:
            print("Well done, you win!")
            break
        else:
            print(str(bulls) + " bulls and " + str(cows) + " cows")
    
def guessNumber():
    while True:
        try:
            if sys.version_info[0] < 3:
                guess=raw_input("Please enter a unique 4 digit number: ")
            else:
                guess=input("Please enter a guess: ")
        except ValueError:
           print("Please enter a valid number")
           continue
       
        if len(set(guess))!=4 or guess.isdigit()==False or len(guess)!=4:
            print("Please make sure your number has four unique digits")
            continue
        else:
            break
        
    return guess

if __name__=="__main__":
    main()