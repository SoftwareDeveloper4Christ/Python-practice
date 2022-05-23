import errno
import random

# Checking if the number is greater than 0
attempt_list = []
def show_score():
    if len(attempt_list) <= 0:
        print("There is currently no high score, it is all yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempt_list)))

# Starting the game
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello Traveller! Welcome to the game of guesses!")

# Request for players name
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))

    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
           guess = input("Pick a number between 1 and 10 ")
        except:
           if int(guess) < 1 or int(guess) > 10:
               raise ValueError("Please guess a number within the given range")
        if int(guess) == random_number:
                print("Nice! You have got it!")
                attempts +=1
                attempt_list.append(attempts)
                print("It took you {} attempts".format(attempts))
    
    # Request for the player to play again
    play_again = input("would you like to play again? Enter Yes/No ")
    
    attempts = 0
    show_score()
    random_number = int(random.randint(1,10))
    if play_again.lower() == "no":
        print("That's cool, have a good day!")
    elif int(guess) > random_number:
        print("It is lower")
    
    attempts +=1
    try:
        if int(guess) < random_number:
            print("It is higher")

    #attempts +=1
    except ValueError as err:
        print("Oh no!, that is not a valid value. Try again...")
        print("{}".format(err))
    else:
        print("That is cool, have a good one!")
    #if __name__=='__main__':
start_game()