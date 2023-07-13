# -*- coding: utf-8 -*-
"""
G. L. Roberts 

15 August 2017

http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

Uses beautifulsoup to parse NYTimes website and print out the top 10 headlines 
and their summaries
"""

import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.nytimes.com/'
    r=requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    headlines=soup.findAll("h2",{"class":"story-heading"})
    summaries=soup.findAll("p",{"class":"summary"})
    headlinesList = [
        storyHeading.text.replace("\n", " ").strip()
        for storyHeading in headlines
    ]
    summariesList = [
        summaryHeading.text.replace("\n", " ").strip()
        for summaryHeading in summaries
    ]
    print("Today's headlines are: ")
    print("-------------------------------------------------------------")

    for i in range(10):
        print(headlinesList[i]+"\n")
        print(summariesList[i]+"\n")
        print("-------------------------------------------------------------")
    
    
if __name__ == "__main__":
    main()

