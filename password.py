import random
import string

def pass_gen(length):
    chars= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

length = int(input("Enter a lenght of the password: "))
print(f"Your password of length {length} --> {pass_gen(length)}")