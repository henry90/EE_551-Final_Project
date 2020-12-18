#Credit: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
#Improved by Yuxiao Shen.

from random import randint

#Create a list of play options
t = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer
computer = t[randint(0,2)]

#Set player to False
player = False

while player == False:
#Set player to True
    #Automatically capitalize on the user's input
    player = input("Rock, Paper, Scissors?").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! :(", "Computer play is:", computer, ".", computer, "covers", player, ".")
        else:
            print("You win!", "Computer play is:", computer, ".", player, "smashes", computer, ".")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! :(", "Computer play is:", computer, ".", computer, "cut", player, ".")
        else:
            print("You win!", "Computer play is:", computer, ".", player, "covers", computer, ".")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! :(", "Computer play is:", computer, ".", computer, "smashes", player, ".")
        else:
            print("You win!", "Computer play is:", computer, ".", player, "cut", computer, ".")
    else:
        print("That's not a valid play. Check your spelling!")
    #Player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    
    #Create a list of play options
t = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer
computer = t[randint(0,2)]

#Set player to False
player = False