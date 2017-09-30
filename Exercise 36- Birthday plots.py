# -*- coding: utf-8 -*-
"""
G. L. Roberts 

30th September 2017

http://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

Similar to the previous exercise, but using the bokeh python library to plot
the histogram instead of matplotlib. 

"""

import json
from collections import Counter
import pandas as pd
from bokeh.plotting import figure, show, output_file

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
    
    x=list(birthdayMonthCount.keys())
    y=list(birthdayMonthCount.values())
    p=figure(x_range=monthNameList)
    p.vbar(x=x,top=y,width=0.5)
    
    show(p)
    
if __name__ == "__main__":
    main()

