import random
print(random.randint(0,6))

random.seed(10)
print(random.random())
#the generator creates a random number based on the seed value, so if the seed value is 10, you will always get 0.5714025946899135 as the first random number.
random.seed(11)
print(random.random())

print(random.randrange(3, 9))
#random.randrange(start, stop, step)

print(random.randint(3, 9))
#This method is an alias for randrange(start, stop+1).

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

x = "WELCOME"
print(random.choice(x))

#https://www.w3schools.com/python/ref_random_choices.asp

# he shuffle() method takes a sequence, like a list, and reorganize the order of the items.
# This method changes the original list, it does not return a new list.
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))
#The sample() method returns a list with a specified number of randomly selected items from a sequence.

print(random.random())
#Return random number between 0.0 and 1.0:

#The uniform() method returns a random floating number between the two specified numbers (both included).
print(random.uniform(20, 60))
# Return a random number between, and included, 20 and 60:
