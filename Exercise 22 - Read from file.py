"""
G. L. Roberts 

25th August 2017

Read lists of prime numbers and happy numbers, and print overlaps
I have done this using sets (because intersections are easy with sets)
"""

def main():
    primeNumbers = {line.strip() for line in open('primeNumbers.txt')}
    happyNumbers = {line.strip() for line in open('happyNumbers.txt')}

    intersect=primeNumbers & happyNumbers
    print(sorted(intersect,key=int))

if __name__=="__main__":
    main()