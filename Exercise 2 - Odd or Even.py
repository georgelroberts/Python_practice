# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Determine whether a number is odd or even
"""

def main():
    number=int(input("Please enter a number: "))
    
    if number%2==0:
        print("Your number is even!")
    else:
        print("Your number is odd!")

    
if __name__ == "__main__":
    main()

