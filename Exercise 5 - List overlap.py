# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Take two lists and return a list containing only the common items
"""
import random

def main():
    firstList=[random.randrange(1, 10) for _ in range(8)]
    secondList=[random.randrange(1, 10) for _ in range(12)]
    
    #Solution asks for no duplicates, so sets are the natural choice
    equal=list(set(firstList)&(set(secondList)))
    print(equal)
    
    # OR if you want list comprehension. Not pretty to remove duplicates
    equal2=[i for i in firstList if i in secondList]
    equal2=list(set(equal2))
    print(equal2)
    
if __name__ == "__main__":
    main()

