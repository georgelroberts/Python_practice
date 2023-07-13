# -*- coding: utf-8 -*-
"""
G. L. Roberts 

14 August 2017

http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

Remove duplicates from a list using 2 methods: sets and a loop
"""

import random

def main():
    testList=[random.randrange(1, 10) for _ in range(10)]
    print(testList)
    dupRemoved1=removDupSets(testList)
    print(dupRemoved1)
    dupRemoved2=removDupLoops(testList)
    print(dupRemoved2)

def removDupSets(testList):
    """ Remove duplicates easily using sets """
    return list(set(testList))

def removDupLoops(testList):
    """ Remove duplicates by checking if each item does not appear twice """
    newList=[]
    for i in testList:
        if i not in newList:
            newList.append(i)
    return newList
    
        
        
if __name__ == "__main__":
    main()

