"""
G. L. Roberts 

9th September 2017

http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

Creates a board class to play tic-tac-toe
"""
import sys
import numpy as np

def main():
    board= Board(3)
    board.printBoard()
    i=0
    while True:
        currentPlayer=i%2+1
        board.getPlay(currentPlayer)
        board.printBoard()
        winner=board.checkWin()

        if winner==3:
            print("The game ended in a draw, try again" )
            break
        elif winner in [1, 2]:
            print(f"The game is over! Player {str(winner)} won the game. Well done!")
            break
        i+=1
            
        
class Board(object):
    """ A class containing everything required for tic-tac-toe """
    def __init__(self, boardSize):
        self.boardSize=boardSize
        self.playBoard=np.array([[0]*boardSize for _ in range(boardSize)])
        self.winner=0
    
    def checkWin(self):
        """ Converts the board into a numpy array to check who has won, if 
        anyone. """
        for i in range(self.boardSize):
            if np.max(self.playBoard[i,:])==np.min(self.playBoard[i,:]) and self.playBoard[i,0]!=0:
                # Check horizontal wins
                self.winner=self.playBoard[i,0]
        for i in range(self.boardSize):
            if np.max(self.playBoard[:,i])==np.min(self.playBoard[:,i]) and self.playBoard[0,i]!=0:
                # Check vertical wins
                self.winner=self.playBoard[i,0]
        
        if np.max(np.diagonal(self.playBoard))==np.min(np.diagonal(self.playBoard)) and self.playBoard[0,0]!=0:
            # Check diagonal wins
            self.winner=self.playBoard[0,0]
        elif np.max(np.diagonal(np.fliplr(self.playBoard)))==np.min(np.diagonal(np.fliplr(self.playBoard))) and np.fliplr(self.playBoard)[0,0]!=0:
            # Check antidiagonal wins
            self.winner=np.fliplr(self.playBoard)[0,0]
        elif 0 not in [elem for sublist in self.playBoard for elem in sublist]:
            # From https://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
            # Game ends in a draw
            self.winner=3
        
        return self.winner # If no winner, self.winner remains as default 0
    
    def printBoard(self):
        """ Prints an aesthetically pleasing game board """
        print(" ---"*self.boardSize)

        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print(f"| {str(self.playBoard[i, j])} ", end='')
            print("|")
            print(" ---"*self.boardSize)
    
    def getPlay(self, player):
        """ Get player response for next play, error checking based on their 
        answer"""
            
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

            if responseTuple[0]>self.boardSize or responseTuple[0]<1:
                print("Please enter a valid x coordinate")
                continue
            elif responseTuple[1]>self.boardSize or responseTuple[1]<1:
                print("Please enter a valid x coordinate")
                continue
            else:
                playX,playY=responseTuple
                playX-=1
                playY-=1
                if self.playBoard[playY,playX]!=0:
                    print("That space is filled already, try again!")
                else:
                    self.playBoard[playY,playX] = 1 if player == 1 else 2
                break


if __name__=="__main__":
    main()