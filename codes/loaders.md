```python
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
```