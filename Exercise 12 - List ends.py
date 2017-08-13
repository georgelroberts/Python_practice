# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

Take a list and make a new list with only the first and last list elements
"""

def main():
    initList=[5,10,15,20,25,35]
    newList=[initList[0],initList[-1]]
    print(newList)

        
if __name__ == "__main__":
    main()

