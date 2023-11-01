#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")



# Define the game logic
def play_rps():
    options = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0
    rounds = 0

    while True:
        # Get user input and convert it to lowercase
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(options)

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            player_wins += 1
        else:
            print("Computer wins this round.")
            computer_wins += 1

        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Game over! You won {player_wins} out of {rounds} rounds.")

# Start the game when the script is run
if __name__ == "__main__":
    play_rps()
