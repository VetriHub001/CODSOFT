import random
import time

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def print_animation(message, delay=0.1):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    
    print("\n____________________ Exciting Rock-Paper-Scissors Battlle____________________\n")
    
    winning_score = int(input("Enter the winning score: "))

    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nLet's see...")
        time.sleep(1)

        print_animation("Rock")
        time.sleep(0.5)
        print_animation("Paper")
        time.sleep(0.5)
        print_animation("Scissors")
        time.sleep(0.5)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print_animation(f"\nResult: {result}")

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}")

        if user_score == winning_score or computer_score == winning_score:
            print("\nGame Over!")
            if user_score == winning_score:
                print_animation("Congratulations! You won!")
            else:
                print_animation("Sorry, you lost. Better luck next time.")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
