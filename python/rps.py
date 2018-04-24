"""
Author: Caleb Muoki
email: muokithedeveloper@gmail.com

A program that will determine the result of a rock paper scissors game
given Player one and player 2 choices.

The rules of the game:
Scissors beat paper
paper beats rock
rock beats  scissors

1. A truth table to help figure out how to code the game

Player1             Player2         Result
Rock                Rock            Tie
Scissors            Scissors        Tie
Paper               Paper           Tie

Rock                Scissors        Player 1
Scissors            Paper           Player 1
Paper               Rock            Player 1

Rock                Paper           Player 2
Scissors            Rock            Player 2
Paper               Scissors        Player 2

"""

# A list of only valid inputs
choices = ["rock", "paper", "scissors"]

# ask for player1 input
player1 = raw_input("Player 1?  ")

# change player1 input to lowercase incase upcase entered
playerOne = player1.lower()

# validate player1 input
while playerOne not in choices:
    print "This is not a valid object selection"
    player1 = raw_input("Player 1?  ")
    playerOne = player1.lower()

# ask for player2 input
player2 = raw_input("Player 2?  ")

# change player2 input to lowercase incase upcase entered
playerTwo = player2.lower()

# validate player2 input
while playerTwo not in choices:
    print "This is not a valid object selection"
    player2 = raw_input("Player 2?  ")
    playerTwo = player2.lower()

# to determine the winnner based on the rules of the game
# and the truth table above
if playerOne == playerTwo:
    print "Tie"

elif playerOne == "rock":
    if playerTwo == "scissors":
        print "Player 1 wins."
    else:
        print "Player 2 wins"

elif playerOne == "paper":
    if playerTwo == "rock":
        print "Player 1 wins."
    else:
        print "Player 2 wins"

elif playerOne == "scissors":
    if playerTwo == "paper":
        print "Player 1 wins."
    else:
        print "Player 2 wins"
