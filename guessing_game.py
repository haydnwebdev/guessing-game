"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import os
import platform
from random import randint


def clear_screen():
    """Detect OS type, perform clear screen."""
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def game_banner():
    """Display Game banner at start of game."""
    message = "Number Guessing Game"
    print("-" * len(message))
    print(message)
    print("-" * len(message))


def start_game():
    """Return a randomly generated number between 1 and 10."""
    return randint(1, 11)


def get_player_guess():
    """Returns a valid integer or a quit signal."""
    while True:
        user_input = input("Choose a number between 1 and 10 or type 'quit' to exit: ")
        # user wants to quit the game
        if user_input.lower() == "quit":
            return "quit"
        # check the integer is valid and within range 1-10
        try:            
            player_guess = int(user_input)
            if player_guess in range(1, 11):
                return player_guess
            else:
                print("Your number must be between 1 and 10. Please try again...")
        except ValueError:
            print("Invalid number entered, please try again...")


def player_stats(high_score, total_games_played):
    """Display player stats at end of game."""
    print("-" * 35)
    print("Player Statistics")
    print("-" * 35)
    print(f"High Score: {min(high_score)}")
    print(f"Total Games Played: {total_games_played}")
    print(f"Previous Attempts: {', '.join(map(str, high_score))}")
    print(f"Average Attempt: {sum(high_score) / len(high_score):.0f}")
    print("-" * 35)


# initialise game variables
high_score = []
player_attempts = 0
total_games_played = 0

# generate random number
number = start_game()

# clear the screen
clear_screen()

# display banner
game_banner()

# start game loop
while True:
    player_guess = get_player_guess()

    if player_guess == "quit":
        print("Exiting the game. Thanks for playing!")
        break

    player_guess = int(player_guess)

    # increment player attempt by 1
    player_attempts += 1

    # Check player's guess and give feedback
    if player_guess < number:
        print("Your guess was too low!")
    elif player_guess > number:
        print("Your was too high!")
    else:
        print("You guessed the number right!")
        total_games_played += 1  # Increment games played
        high_score.append(player_attempts)  # Add total attempts to high score list

        # Check if the player wants to continue
        if input("Play again? y/n: ").lower() == 'y':
            number = start_game()  # Generate new number
            player_attempts = 0  # Reset player attempts
        else:
            print("Thanks for playing the number guessing game!")
            player_stats(high_score, total_games_played)  # Display player stats
            break
