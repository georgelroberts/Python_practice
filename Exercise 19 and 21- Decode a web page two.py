"""
G. L. Roberts 

16th August 2017

Take a multi-page article from vanity fair and make a single page. 
"""
import requests
from bs4 import BeautifulSoup

def main():
    r=requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture","html")
    soup=BeautifulSoup(r.text)
    
    with open('varsityArticle.txt','w') as open_file:
        open_file.write(soup.title.text+"\n\r\n\r")
        
        subtitle=soup.find_all('div',{"class:","dek"})
        for part in subtitle:
            open_file.write(part.text+"\n\r\n\r")
        
        content=soup.find_all('section',{"class:","content-section"})
        for part in content:
            open_file.write(part.text+"\n\r\n\r")
    
    
if __name__=="__main__":
    main()