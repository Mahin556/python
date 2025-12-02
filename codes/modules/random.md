
```python
import random   # import the random module

# random.random()
# Returns a float between 0.0 and 1.0
print(random.random())

# random.uniform(a, b)
# Returns a float between a and b (inclusive)
print(random.uniform(10, 20))

# random.randint(a, b)
# Returns an integer between a and b (inclusive)
print(random.randint(1, 6))   # like rolling a dice

# random.randrange(start, stop, step)
# Returns a number from the range with a step
print(random.randrange(1, 10, 2))   # returns 1,3,5,7,9


# ------------------------------------------------------------
# RANDOM CHOICES FROM LISTS
# ------------------------------------------------------------

colors = ["red", "blue", "green", "yellow"]

# random.choice()
# Selects one random item from a list
print(random.choice(colors))
#blue

# random.choices()
# Selects multiple items with replacement (items CAN repeat)
print(random.choices(colors, k=3))
#['green', 'blue', 'green']

# random.sample()
# Selects multiple items WITHOUT replacement (items DO NOT repeat)
print(random.sample(colors, 2))
#['green', 'yellow']


# ------------------------------------------------------------
# SHUFFLING LISTS
# ------------------------------------------------------------

# random.shuffle(list)
# Shuffles items IN PLACE (modifies the original list)
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)


# ------------------------------------------------------------
# SEEDING THE RANDOM GENERATOR
# ------------------------------------------------------------

# random.seed(n)
# Makes random numbers repeat every time you run the program
# Useful for testing and debugging
random.seed(42)
print(random.random())   # will always give the same output when seed=42


random.seed(42)
print(random.random()) 
random.seed(33)
print(random.random()) 
random.seed(42)
print(random.random()) 
random.seed(33)
print(random.random()) 

# $ python test.py 
# 0.6394267984578837
# 0.5703284231368732
# 0.6394267984578837
# 0.5703284231368732


# ------------------------------------------------------------
# RANDOM DISTRIBUTIONS (USEFUL FOR SIMULATION / ML)
# ------------------------------------------------------------

# random.gauss(mu, sigma)
# Returns a number from Gaussian/Normal distribution
print(random.gauss(0, 1))

# random.triangular(low, high, mode)
# Skewed distribution with a specified peak
print(random.triangular(1, 10, 5))

# random.expovariate(lambda)
# Exponential distribution (e.g. waiting times)
print(random.expovariate(1.5))


# ------------------------------------------------------------
# SECURITY NOTE
# ------------------------------------------------------------

# DO NOT use random for passwords or tokens.
# Instead use the 'secrets' module for cryptographic randomness:
# import secrets; secrets.token_hex(16)


# ------------------------------------------------------------
# COMPLETE EXAMPLES
# ------------------------------------------------------------

# Dice roll simulation (100 rolls)
dice_rolls = [random.randint(1, 6) for _ in range(100)]
print(dice_rolls[:10])  # show only first 10

# Generate random 12-character password
import string
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for _ in range(12))
print("Password:", password)

# Shuffle a deck of cards
deck = [f"{value}{suit}" for value in "A23456789JQK" for suit in "♠♥♦♣"]
random.shuffle(deck)
print("Some cards:", deck[:10])   # print first 10 cards after shuffle


#---

x = "WELCOME"
print(random.choice(x))




```
