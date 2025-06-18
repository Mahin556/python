# Generate a random number between 1 and 100 and let the user guess it.
# User guess a number between 1 and 100.
# User see if their guess is too high, too low, or correct.
# If the guess is correct, the user is congratulated and the number of attempts is displayed.
# do it in a loop until the user exits the game.
import random

random_number = random.randint(1, 100)
guess_count = 0

while True:
    while True:
        guessed_number = int(input("Guess a number between 1 and 100: "))
        if guessed_number < 1 or guessed_number > 100:
            print("Please guess a number between 1 and 100.")
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