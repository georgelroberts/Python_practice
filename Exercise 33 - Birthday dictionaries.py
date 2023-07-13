# -*- coding: utf-8 -*-
"""
G. L. Roberts 

30th September 2017

http://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

Use a dictionary of people's birthdays and allow a user to print out each date. 
'quit' allows the user to exit. Users can also add birthdays to the dictionary. 
"""

import sys

def main():
    birthdayDict = {
            "matt":"02/11/91",
            "cora":"26/10/91",
            "george":"27/07/92",
            "bill":"23/03/84"
            }
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    printAllDictKeys(birthdayDict)
    while True:
        name=inputName()
        if name=="quit":
            break
        print(birthdayDict.get(name,"We don't have that name yet."))
        if name not in birthdayDict:
            birthday=inputBirthday()
            if birthday=="quit":
                break
            else:
                birthdayDict[name]=birthday
    
def printAllDictKeys(birthdayDict):
    for key in birthdayDict:
        print(key.title())
    return 0    
    
def inputName():
    """ Gets user input and makes sure it is valid"""
    while True:
        try:
            if sys.version_info[0] < 3:
                name=raw_input("Whose birthday would you like to know? (or quit) ")
            else:
                name=input("Whose birthday would you like to know? (or quit) ")
        except ValueError:
        	print("Please enter a valid name")
        	continue
        
        break
        
    return name.lower()

def inputBirthday():
    """ Gets user input and makes sure it is valid"""
    while True:
        try:
            if sys.version_info[0] < 3:
                birthday=raw_input("Please enter a birthday if you would like to add it: (or quit) ")
            else:
                birthday=input("Please enter a birthday if you would like to add it: (or quit) ")
        except ValueError:
        	print("Please enter a valid birthday")
        	continue
        break
        
    return birthday.lower()

if __name__ == "__main__":
    main()

