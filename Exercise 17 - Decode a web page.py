# -*- coding: utf-8 -*-
"""
G. L. Roberts 

15 August 2017

http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

Uses beautifulsoup to parse NYTimes website and print out the top 10 headlines 
and their summaries"""

import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.nytimes.com/'
    r=requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    headlines=soup.findAll("h2",{"class":"story-heading"})
    summaries=soup.findAll("p",{"class":"summary"})
    headlinesList=[]
    summariesList=[]
    for storyHeading in headlines:
        headlinesList.append(storyHeading.text.replace("\n"," ").strip())
    for summaryHeading in summaries: 
        summariesList.append(summaryHeading.text.replace("\n"," ").strip())
    
    print("Today's headlines are: ")
    print("-------------------------------------------------------------")
    
    for i in range(10):
        print(headlinesList[i]+"\n")
        print(summariesList[i]+"\n")
        print("-------------------------------------------------------------")
    
    
if __name__ == "__main__":
    main()

