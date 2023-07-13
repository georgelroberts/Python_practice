# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Ask for a number then print a list of all of its divisors
"""
import math

def main():
    initNumber=int(input("Please enter a number: "));
    divisorList=[1]

    divisorList.extend(
        i
        for i in range(2, math.ceil(initNumber / 2) + 1)
        if initNumber % i == 0
    )
    print(divisorList)
    
if __name__ == "__main__":
    main()

