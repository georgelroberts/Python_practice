# -*- coding: utf-8 -*-
"""
G. L. Roberts 

14 August 2017

http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

Take a string of words and reverse the word order
"""

def main():
    testString= "My name is George" 
    print(reverseWordOrder(testString))
    
def reverseWordOrder(testString):
    """ Reverse string by creating a new string """
    testString=testString.split(" ")
    newString=[]
    for i in range(len(testString)):
        newString.append(testString[-i-1])
    return newString    
        
        
if __name__ == "__main__":
    main()

