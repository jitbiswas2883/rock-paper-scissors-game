import random

print("🎮 Welcome to Rock,Paper, Sessiors Game 🎮")

options = ["rock","paper","scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice(rock, paper, scissors) :").lower()
    computer_choice = random.choice(options)
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    print(f"You choose:{user_choice}")
    print(f"Computer choose:{computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif(user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You Win this round!")
        user_score += 1
    else:
        print("Computer Win this round!")
        computer_score += 1
    print(f"Your score: {user_score} | Computer score: {computer_score}")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break








































































































































































