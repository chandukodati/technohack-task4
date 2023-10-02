import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif player_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif player_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

while True:
    # Get user's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Validate user's choice
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        continue
    # Get computer's choice
    computer_choice = get_computer_choice()

    # Determine the winner
    result = determine_winner(player_choice, computer_choice)

    # Display the choices and result
    print(f"You chose {player_choice}. Computer chose {computer_choice}.")
    print(result)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
