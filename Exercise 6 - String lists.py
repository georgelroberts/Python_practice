# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

See whether user's string is a palindrome
"""

def main():
    userString=input("Palindrome tester: ").lower()
    userStringLength=len(userString)
    userStringReversed=""
    for i in range(userStringLength):
        userStringReversed=userStringReversed+userString[-i-1]
    if userString==userStringReversed:
        print("Palindrome alert!")
    else:
        print("That was not a palindrome")
        
if __name__ == "__main__":
    main()

