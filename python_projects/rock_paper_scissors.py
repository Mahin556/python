# User Won conditions
# User  Computer
# rock  scissors
# paper  rock
# scissors paper

import random
choices = ["rock", "paper", "scissors"]
while True:
    computer_choice = random.choice(choices)
    user_choice = int(input("Choices:\n1 -> rock\n2 -> paper\n3 -> scissors\n4 -> exit\nEnter your Choice: "))
    if user_choice == 1:
        choice_name = 'rock'
    elif user_choice == 2:
        choice_name = 'paper'
    elif user_choice == 3:
        choice_name = 'scissors'
    elif user_choice == 4:
        exit()
    else:
        print("Enter a valid chooice")

    print(f"Computer Choice: {computer_choice}")
    if choice_name == computer_choice:
        print("It's a tie!")
    elif (computer_choice == "scissors" and choice_name == "rock") or (computer_choice == "rock" and choice_name == "paper") or (computer_choice == "paper" and choice_name == "scissors"):
        print("You won!")
    else:
        print("Computer win!")

    # Ask if the user wants to play again
    #print("Do you want to play again? (Y/N)")
    #ans = input().lower()
    #if ans == 'n':
    #   break
    


