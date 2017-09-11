# -*- coding: utf-8 -*-
"""
G. L. Roberts 

14 August 2017

http://www.practicepython.org/solution/2014/07/25/13-fibonacci-solutions.html

Calculate n fibonacci numbers
"""

def main():
    n=getInt("Please enter a number: ")
    fibArray=[1]
    if n==1:
        print(fibArray)
    else:
        fibArray.append(1)
        for i in range(n-2):
            fibArray.append(fibArray[i]+fibArray[i+1])
        print(fibArray)
        

def getInt(string):
    """ Get a positive integer from the user """
    while True:
        try:
            userNo=int(input(string))
        except ValueError:
            print("Sorry, try again please")
            continue
        
        if userNo < 0:
            print("Sorry, try again please")
            continue
        else:
            break
    return userNo
        
if __name__ == "__main__":
    main()

