
"""
G. L. Roberts 

26th September 2017

http://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

Implement my own max() function. Task asks for just three, but this will 
work for a list of any size

"""

def main():
	listToMax=[77,3,98]

	print(maximise(listToMax))

def maximise(listToMax):
	for i in range(len(listToMax)):
		if i==0:
			maxNo=listToMax[i]
		if listToMax[i]>maxNo:
			maxNo=listToMax[i]

	return maxNo


if __name__ == "__main__":
    main()
