for i in range(1,6):
    print(i)

i=1
while (i<6):
    print(i)
    i+=1


l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]
i=0
while (i<len(l)):
    print(l[i])
    i+=1

for i in l:
    print(i)

h="Harry"
for i in h:
    print(i)
else:
    print("Done")


for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)


for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)


for i in range(100):
    if(i == 34):
        pass # it is null statement which do nothing

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Example
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
# Example
for x in [0, 1, 2]:
  pass

