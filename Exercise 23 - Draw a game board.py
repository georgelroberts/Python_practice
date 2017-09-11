"""
G. L. Roberts 

31st August 2017

http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

Creates an nxm game board for tic-tac toe. 
"""

def main():
    printBoard(3)
    
def printBoard(n,m=0):
    """ Draws a blank playing board for tic-tac-toe """
    #If just one argument, create nxn grid
    if m==0:
        m=n
    
    sideString=''
    vertString=''
    for i in range(n):
        sideString+=' ----'
        vertString+='|    '
    vertString+='|'
    
    for i in range(m):
        print(sideString+'\n'+vertString)
    print(sideString)
        
if __name__=="__main__":
    main()