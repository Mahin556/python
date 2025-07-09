#String Format

age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# Escape Characters
# \'	Single Quote	
# \""	Double Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# \ooo	Octal Value	print("\141")	a
# \xhh	Hex Value	print("\x61")	a
# \r	Carriage Return	print("12345\rAB")	AB345

#"\r" moves the cursor to the beginning of the current line — but does not go to the next line. So, anything you write after \r will overwrite from the beginning of the same line.

print("12345\rAB")
#Output:
#AB345

import time
for i in range(5):
    print(f"\rLoading {'.' * (i + 1)}", end="")
    time.sleep(1)

# Countdown Timer
import time
for i in range(5, 0, -1):
    print(f"\rCountdown: {i} seconds left", end="")
    time.sleep(1)

print("\nTime's up!")


#Spinner Animation
spinner = ['|', '/', '-', '\\']
for _ in range(10):
    for symbol in spinner:
        print(f"\rProcessing {symbol}", end="")
        time.sleep(0.2)

print("\nDone!")

#Progress bar
for i in range(1, 21):
    bar = '#' * i + '-' * (20 - i)
    print(f"\rProgress: [{bar}] {i*5}%", end="")
    time.sleep(0.2)

print("\nTask Completed!")


# Dot Loader
for _ in range(3):
    for dots in ['.', '..', '...']:
        print(f"\rLoading{dots}", end="")
        time.sleep(0.5)

print("\nLoaded!")

print("Typing...", end="")
time.sleep(2)
print("\rErased     ", end="")  # Overwrites the same line

print("\nDone.")
