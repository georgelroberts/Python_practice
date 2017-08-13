# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Take a list and print all the elements that are <10
"""

def main():
    testList=[1,1,2,3,5,8,13,21,34,55,89]
    filteredList=[i for i in testList if i<5]
    print(filteredList)
    
if __name__ == "__main__":
    main()

