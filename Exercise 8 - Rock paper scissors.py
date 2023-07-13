# -*- coding: utf-8 -*-
"""
G. L. Roberts 

13 August 2017

http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Two player rock paper scissors game.

Exceptions from https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
"""

def main():
    player1Points=0
    player2Points=0
    while True:
        print("Please enter 'rock', 'paper' or 'scissors': ")
        player1=getUserMove("1")
        player2=getUserMove("2")

        if player1==player2:
            print("It's a draw!")
            player1Points=player1Points+1
            player2Points=player2Points+1

        elif ((player1=='rock' and player2=='scissors') or
              (player1=='paper' and player2=='rock') or
              (player1=='scissors' and player2=='paper')):
            print("Player 1 wins!")
            player1Points=player1Points+1

        else:
            print("\nPlayer 2 wins!")
            player2Points=player2Points+1

        playAgain = input("Do you want to play again? (Y/N): ").lower()
        if playAgain=='n':
            break

    if player1Points==player2Points:
        print(f"It was a draw{player1Points}all!")
    elif player1Points>player2Points:
        print(f"Player 1 wins {str(player1Points)} to {str(player2Points)}")
    else:
        print(f"Player 2 wins {str(player2Points)} to {str(player1Points)}")
          
    
def getUserMove(player):
    """ Get user input for rock paper or scissors """
    while True:
        try:
            playerMove = input(f"Player{player}: ").lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if playerMove in ['rock', 'paper', 'scissors']:
            break
        print("Sorry, I didn't understand that.")
        continue
    return playerMove
    
        
if __name__ == "__main__":
    main()

