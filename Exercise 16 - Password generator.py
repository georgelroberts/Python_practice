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
    print(f"Your password is: {password}")
    
def getInt(string):
    """ Get a valid password length """
    while True:
        try:
            userNo=int(input(string))
        except ValueError:
            print("Sorry, try again please")
            continue

        if userNo > 0:
            break
        print("Sorry, try again please")
        continue
    return userNo  

def passwordGen(strength, n):
    """Generate the choice of letters based on the password strength, then
    randomly pick letters for the password. """
    password=''
    if strength == 'medium':
        choice=string.ascii_letters
    elif strength == 'strong':
        choice=string.printable
    elif strength == 'weak':
        choice=string.ascii_lowercase
    for _ in range(n):
        password = password + random.choice(choice)
    return password

        
if __name__ == "__main__":
    main()

