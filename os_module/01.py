import os

def current_dir():
    cwd=os.getcwd()
    print(cwd)

current_dir() #give cwd
os.chdir("../") #change cwd
current_dir()

