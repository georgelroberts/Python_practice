# -*- coding: utf-8 -*-
"""
G. L. Roberts 

30th September 2017

http://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

Takes the birthdays from a JSON file on disk. Allows the user to update this 
file. Uses a dictionary inside the program for access to save repeated file 
reads. User has to input the date as dd/mm/yyyy to make exercise 35 work 
correctly.

"""

import sys
import json

def main():
    with open("birthdays.json","r") as f:
        birthdayDict=json.load(f)
    
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    printAllDictKeys(birthdayDict)
    while True:
        name=inputName()
        if name=="quit":
            break
        else:
            print(birthdayDict.get(name,"We don't have that name yet."))
            if name not in birthdayDict:
                birthday=inputBirthday()
                if birthday=="quit":
                    break
                else:
                    birthdayDict[name]=birthday
                    with open("birthdays.json","w") as f:
                        json.dump(birthdayDict,f)

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
                birthday=raw_input("Please enter a birthday (dd/mm/yyyy) if you would like to add it: (or quit) ")
            else:
                birthday=input("Please enter a birthday (dd/mm/yyyy) if you would like to add it: (or quit) ")
        except ValueError:
        	print("Please enter a valid birthday")
        	continue
        if (
            len(birthday) != 10 or birthday[2] != '/' or birthday[5] != '/'
            or int(birthday[0:2])<1 or int(birthday[0:2])>31
            or int(birthday[3:5])>12 or int(birthday[3:5])<0
            ):
            print("Please enter a valid birthday as dd/mm/yyyy")
            continue
        else:
            break
        
    return birthday.lower()

if __name__ == "__main__":
    main()

