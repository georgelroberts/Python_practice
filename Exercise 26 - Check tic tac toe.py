# -*- coding: utf-8 -*-
"""
G. L. Roberts 

6th September 2017

Defines a function that calculates whether a game of tic-tac-toe has been won,
where the board is a list of lists, with 0 denoting no entrant and 1 and 2 
meaning that player has placed a tile there. 
This will work for any size board.
"""

import numpy as np

def main():
    board=np.array([[0, 2, 1],
	[2, 1, 0],
	[2, 1, 0]])

    
    print(checkWin(board))
    
    
def checkWin(board):
    """ Converts the board into a numpy array to check who has won, if anyone. """
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
    
if __name__=="__main__":
    main()

