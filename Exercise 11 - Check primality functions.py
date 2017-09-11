# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Check if a number is a prime. I borrow my solution from problem 4.
"""

import math

def main():
    userNo=getInt("Please enter a number: ")
    if len(divisors(userNo))==1 and userNo!=1:
        print("Number is a prime! ")
    else:
        print("Number is not a prime." )
    
def getInt(string):
    """ Get a valid number from the user"""
    while True:
        try:
            userNo=int(input(string))
            break
        except ValueError:
            print("Sorry, try again please")
            continue
    return userNo

def divisors(initNumber):
    """ Return a list of the valid devisors of a number using a for loop """
    divisorList=[1]
    
    for i in range(2,math.ceil(initNumber/2)+1):
        if initNumber%i==0:
            divisorList.append(i)
            
    return divisorList

        
if __name__ == "__main__":
    main()

