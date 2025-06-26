import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        # For printing the empty spaces for letters of the word
        print("_",end=" ")
    print()

    guessed=''
    chances = len(word) + 2
    flag = 0

    try:
        while (chances != 0) and flag == 0: # Flag is updated when the word is correctly guessed
            try: 
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
    

    

