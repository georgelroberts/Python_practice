# -*- coding: utf-8 -*-
"""
G. L. Roberts 

26th September 2017

http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

Pick a random work from the SOWPODS dictionary from the link 
http://norvig.com/ngrams/sowpods.txt. 
Works using 'requests' if file isn't downloaded
"""

import random
import requests
import os

def main():
	print(getRandWord())
    
def getRandWord():
	if os.path.isfile('./wordList.txt'):
		with open('wordList.txt') as file:
			dataList=file.read().splitlines()
	else:
		data = requests.get('http://norvig.com/ngrams/sowpods.txt')
		dataList=data.text.split('\r\n')
	return dataList[random.randint(0,len(dataList))]


if __name__ == "__main__":
    main()

