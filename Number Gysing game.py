
							# *********Number Gassing********* 

# GuitHub : 

# Source code:
"""
 
This is a number guessing game.
The player have to guess the number choosen by the computer randomly.
The player has Seven attempt to guess the number.
If the player has guessed the number in any of the Seven attempts that means the player has won the game.
But if the player would not be able to guess the number in Seven attempts the player will lose the game.
If the user won the game our program will show the number of attempts taken by the player to won the game.
That's it! :)
 
"""
 
 
import random
MIN_LIMIT = 1
MAX_LIMIT = 100
NUMBER_OF_ATTEMPT = 7
 
def main():
 
    # printing the intro of the game
    print_intro()
 
    # Storing the number choosen by computer
    secret_number = random.randint(MIN_LIMIT,MAX_LIMIT)
 
    #Calculate if the player won or lose the game and then shows the result
    calculate_win_or_lose(secret_number)
 
 
def print_intro():
    print("Number Guessing Game :")
    print("")
    print("choose a number between 1 and 100")
    print("You have five attempts to guess the number, ")
    print("if you will get the correct guess you will win the game")
    print("")
 
 
def calculate_win_or_lose(secret_number):
    for i in range (NUMBER_OF_ATTEMPT) :
        guess = int(input("Enter your guess : "))
        if guess == secret_number :
            print("Congratulations! you guessed the number in", i, "attempts." )
            return
        elif guess < secret_number :
            print("Your number is too low.")
            print("")
        else :
            print("Your number is too high.")
            print("")
    print("You lose the game, the original number was", secret_number,", better luck next time!")
 
 
if __name__ == '__main__':
    main()
    