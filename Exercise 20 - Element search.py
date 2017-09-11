# -*- coding: utf-8 -*-
"""
G. L. Roberts 

16 August 2017

http://www.practicepython.org/exercise/2014/11/11/20-element-search.html

Build a function to implement a binary search on a random list 
(to find the value 10)
"""

import random

def main():
    unsortedList=random.sample(range(200),100)
    sortedList=sorted(unsortedList)
    print(binarySearch(sortedList,10))
    
def binarySearch(sortedList,n):
    """ Implements the binary search """
    lowVal=0
    highVal=len(sortedList)-1
    while lowVal<=highVal:
        halfWay=(lowVal+highVal) //2
        if sortedList[halfWay]<n:
            lowVal=halfWay+1
        elif sortedList[halfWay]>n:
            highVal=halfWay-1
        else:
            return True
    return False
    

if __name__ == "__main__":
    main()

