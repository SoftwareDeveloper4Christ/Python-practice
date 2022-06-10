# Building Rock-Paper-Scissors game

# First, we import necessary modules
import random

#Create a list to store all possible options
game_list = ["Rock","Paper","Scissors"]
    
CPU_list = random.choice(game_list)

# Take in user input
Player = input("Enter an option between (Rock, Paper or Scissors): ")

# Determining a Winner
while True:
    if Player == CPU_list:
        print("It is a tie!")
    elif Player != game_list:
        print("Error")
    Player = input("Enter an option between (Rock, Paper or Scissors): ")
    
    if Player == "Rock":
        if CPU_list == "Scissors":
            print("Rock beats Scissors. You win!!!")
        else:
            print("Paper beats Rock. You lose!")
    elif Player == "Paper":
        if CPU_list == "Rock":
            print("Paper beats Rock. You win!!!")
        else:
            print("Scissors beats Paper. You lose!")
    elif Player == "Scissors":
        if CPU_list == "Paper":
            print("Scissors beats Paper. You win!!!")
        else:
            print("Rock beats Scissors. You lose!")