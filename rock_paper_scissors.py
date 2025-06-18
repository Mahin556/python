# User Won conditions
# User  Computer
# rock  scissors
# paper  rock
# scissors paper

import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

user_choice = str(input("Choose between rock, paper, scissors: "))

print(f"Computer Choice: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (computer_choice == "scissors" and user_choice == "rock") or (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors"):
    print("You won!")
else:
    print("Computer win!")



