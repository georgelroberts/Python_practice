# -*- coding: utf-8 -*-
"""
G. L. Roberts 

30th September 2017

http://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

Takes the JSON file from the previous exercise and counts the frequencies of 
birthdays in each month. Then plots the histogram of these using pandas and 
matplotlib.

"""

import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def main():
    with open("birthdays.json","r") as f:
        birthdayDict=json.load(f)
    
    birthdayMonthList=[]
    monthNameList=["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    for key in birthdayDict:
        # Matches the number of the month in the JSON file to the month name list
        birthdayMonth=monthNameList[int(birthdayDict[key][3:5])-1]
        birthdayMonthList.append(birthdayMonth)
        
    birthdayMonthCount=Counter(birthdayMonthList)
    
    print(birthdayMonthCount)
    
    months=birthdayMonthCount.keys()
    
    df=pd.Series(birthdayMonthCount,index=months)
    df.plot(kind='bar')
    plt.show()


if __name__ == "__main__":
    main()

