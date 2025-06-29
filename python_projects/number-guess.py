# Generate a random number between 1 and 100 and let the user guess it.
# User guess a number between 1 and 100.
# User see if their guess is too high, too low, or correct.
# If the guess is correct, the user is congratulated and the number of attempts is displayed.
# do it in a loop until the user exits the game.
import random

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

random_number = random.randint(low, high)
guess_count = 0

while True:
    while True:
        guessed_number = int(input(f"Guess a number between {low} and {high}: "))
        if guessed_number < low or guessed_number > high:
            print(f"Please guess a number between {low} and {high}.")
            continue
        guess_count += 1
        if guessed_number < random_number:
            print("Your guess is too low.")
        elif guessed_number > random_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {guess_count} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    guess_count = 0
    if play_again != 'yes':
        break