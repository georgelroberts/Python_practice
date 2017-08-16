"""
G. L. Roberts 

16th August 2017

Take a multi-page article from vanity fair and make a single page. 
"""
import requests
from bs4 import BeautifulSoup

def main():
    r=requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture","html.parser")
    soup=BeautifulSoup(r.text)
    print(soup.title.text)
    print("\n")
    subtitle=soup.find_all('div',{"class:","dek"})
    for part in subtitle:
        print(part.text)
    content=soup.find_all('section',{"class:","content-section"})
    
    for part in content:
        print(part.text)
        print("\n")

if __name__=="__main__":
    main()