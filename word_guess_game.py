import random

name = input("What is your name? ")
print(f"Good Luck ! {name}")

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 
        'player', 'condition', 'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess a character")

guesses = ''
turns = 12

while turns > 0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1

    if failed == 0:
        print("You Won!")
        print("The word is: ", word)
        break

    print()
    guess=input("guess the char: ")
    guesses += guess

    if guess not in word:
        turns-=1
        print('wrong')
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")

