# -*- coding: utf-8 -*-
"""
G. L. Roberts 

15 August 2017

http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

Take a string of words and reverse the word order
"""

import random
import string

def main():
    pasStrength=input("Please enter password strength (weak, medium, strong): ")
    pasStrength=pasStrength.lower()
    pasLength=getInt("Please enter your password length: ")
    password=passwordGen(pasStrength,pasLength)
    print("Your password is: "+password)
    
def getInt(string):
    while True:
        try:
            userNo=int(input(string))
        except ValueError:
            print("Sorry, try again please")
            continue
        
        if userNo <= 0:
            print("Sorry, try again please")
            continue
        else:
            break
    return userNo  

def passwordGen(strength, n):
    password=''
    if strength=='weak':
        choice=string.ascii_lowercase
    elif strength=='medium':
        choice=string.ascii_letters
    elif strength=='strong':
        choice=string.printable
    for i in range(n):
            password = password + random.choice(choice)
    return password

        
if __name__ == "__main__":
    main()

