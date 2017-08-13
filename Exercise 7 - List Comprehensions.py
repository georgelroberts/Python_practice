# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

Find even numbers of a list using list comprehensions
"""

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(evenNumbers(a))

def evenNumbers(inputList):
    return [i for i in inputList if i%2==0]
    
        
if __name__ == "__main__":
    main()

