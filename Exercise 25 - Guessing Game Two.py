"""
G. L. Roberts 

4th September 2017

Opposite of the first guessing game: The user says a number 0-100, then the 
computer will try to get it. Responses are high (h), low (l) or your number (c)
TODO: Fix troubleshooting
"""
import sys

def main():
    userNo = storeNumber()
    
    print("Now tell me if my guess is too high (h), low (l) or is correct (c)")
    
    guess=50
    response='NULL'
    high=100
    low=0
    
    while response !='c':
        print("Guess: " + str(guess))
        response=getResponse()
        if guess==userNo:
            if response=='c':
                print("Hurrah, you have done it!")
            else:
                print("The user cheated (you still win)!")
            break
        elif response=='e':
            break
        elif response=='h':
            high=guess
            guess-=int((high-low)/2.0) # divide remaining potential by 2
        elif response=='l':
            low=guess
            guess+=int((high-low)/2.0)
        elif response=='c':
            if guess==userNo:
                print("Hurrah, you have done it!")
            else:
                print("I believe the user got a little confused!")
            break
    
def storeNumber():
    """ Stores the user's initial number """
    while True:
        try:
            if sys.version_info[0] < 3:
                guess=int(raw_input("Please enter a number between 0 and 100: "))
            else:
                guess=int(input("Please enter a number between 0 and 100: "))
        except ValueError:
            print("Please enter a valid number")
            continue
       
        if guess<0 or guess>100:
            print("Please make sure your number is between 0 and 100")
            continue
        else:
            break
        
    return guess

def getResponse():
    """ User's response to computer guess """
    while True:
        try:
            if sys.version_info[0] < 3:
                response=raw_input("Response: ")
            else:
                response=input("Response: ")
        except ValueError:
            print("Please enter a valid response")
            continue
        
        if response not in ['h','l','c','e']:
            print("Please give me a correct response, or type 'e' to end")
            continue
        else:
            break
        
    return response


if __name__=="__main__":
    main()