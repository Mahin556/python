import random

def game():
    print("Playing game....")
    new_score=random.randint(1,62)
    with open("Hi-score.txt","r") as f:
        high_score=f.read()
        if (high_score!=""):
            high_score=int(high_score)
        else:
            high_score=0

    print(f"Your score: {new_score}")
    if (new_score > high_score):
        with open("Hi-score.txt","w") as f:
            f.write(str(new_score))    

game()