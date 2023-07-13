"""
G. L. Roberts 

9th September 2017

http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

Complete tic-tac-toe game. Users can create a square board of any size.

Taken functions from other solutions
"""
import sys
import numpy as np

def main():
    boardSize=3
    board = drawPlayBoard(boardSize)
    printBoard(board,boardSize)
    i=0
    while True:
        while True:
            play=getPlay(i%2+1,boardSize)
            playX,playY=play
            playX-=1
            playY-=1
            if board[playX][playY]!=0:
                print("That space is filled already, try again!")
            else:
                break

        board[playX][playY] = 1 if i%2 == 0 else 2
        printBoard(board,boardSize)

        i+=1

        winner=checkWin(board)
        if winner!=0:
            print(f"The game is over! Player {str(winner)} won the game. Well done!")
            break
        elif 0 not in [elem for sublist in board for elem in sublist]:
            # From https://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
            print("The game ended in a draw, try again" )
        
    
def drawPlayBoard(x,y=0):
    """ Draw the initial playing board. If y isn't defined, this is a square 
    board"""
    if y==0:
        y=x
    return [[0]*y for _ in range(x)]
    

def getPlay(player, x,y=0):
    """ Get player response for next play, error checking based on their 
    answer"""
    if y==0:
        y=x

    while True:
        try:
            if sys.version_info[0] < 3:
                response = raw_input(
                    f"Player {str(player)}, please enter your play in the form X,Y: "
                )
            else:
                response = input(
                    f"Player {str(player)}, please enter your play in the form X,Y: "
                )
        except ValueError:
            print("Please enter a valid response")
            continue

        response.strip().split(",")
        responseTuple=(int(response[0]),int(response[2]))

        if responseTuple[0]>x or responseTuple[0]<1:
            print("Please enter a valid x coordinate")
            continue
        elif responseTuple[1]>y or responseTuple[1]<1:
            print("Please enter a valid x coordinate")
            continue
        else:
            break

    return responseTuple

def checkWin(board):
    """ Converts the board into a numpy array to check who has won, if 
    anyone. """
    board=np.array(board)
    boardShape=np.shape(board)
    
    for i in range(boardShape[0]):
        if np.max(board[i,:])==np.min(board[i,:]) and board[i,0]!=0:
            return board[i,0]
    for i in range(boardShape[1]):
        if np.max(board[:,i])==np.min(board[:,i]) and board[0,i]!=0:
            return board[0,i]
    
    if np.max(np.diagonal(board))==np.min(np.diagonal(board)) and board[0,0]!=0:
        return board[0,0]
    elif np.max(np.diagonal(np.fliplr(board)))==np.min(np.diagonal(np.fliplr(board))) and board[0,0]!=0:
        return np.fliplr(board)[0,0]
    else:
        return 0
    
def printBoard(board,boardSize):
    """ Prints an aesthetically pleasing game board """
    board=np.array(board)
    print(" ---"*boardSize)

    for i in range(boardSize):
        for j in range(boardSize):
            print(f"| {str(board[j, i])} ", end='')
        print("|")
        print(" ---"*boardSize)
    
        
if __name__=="__main__":
    main()