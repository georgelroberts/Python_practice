# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Ask user for name and age. Print out when they will turn 100.
"""

def main():
    name=input("What is your name? ")
    age=int(input("And your age? "))
    
    currentYear=2017;
    turn100=str(100-age+currentYear)
    print("You will be 100 in "+ turn100 +" "+name+".")
    
if __name__ == "__main__":
    main()

