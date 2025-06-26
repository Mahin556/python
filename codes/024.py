l1=["mahin","apple","mahin",22,5.11,True,None]
t1=tuple(l1) #touple constructor
t2=("mahin","apple","mahin",22,5.11,True,None)
print(type(t1))
print(type(t2))

a=() # empty tuple
print(type(a))
b=(1,) # tuple with one element
print(type(b))

#
# no append no insert, no pop, no remove
# tuples are faster then list

new=l1.count(22)
print(new)

index=l1.index(22)
print(index)

print(len(l1))


#tuple without parenthesis 
guitars = 'yamaha', 'baton rouge', 'taylor' 
print(type(guitars))

# tuple unpacking
guitarists=('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitaristi, guitarist, guitarist3 = (guitarists)
print (guitarist)


# list inside tuples
favorites = ('southern magnolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()

new1=l1[1:4]
print(new1)

fruites=[]
print("Enter a fruites name:")
fruites.append(input("Enter first fruite name:"))
fruites.append(input("Enter second fruite name:"))
fruites.append(input("Enter third fruite name:"))
fruites.append(input("Enter fourth fruite name:"))
fruites.append(input("Enter fifth fruite name:"))
fruites.append(input("Enter sixth fruite name:"))
fruites.append(input("Enter seven fruite name:"))
print(fruites)

num=range(1,5)
print(sum(num))

num=(1,3,0,0,0)
print(num.count(0))

def tuple_(num1,num2):
    sum=num1+num2
    multi=num1*num2
    return sum, multi

print(type(tuple_(3,2)))

type_=tuple(range(0,6))
print(type_)
print(type(type_))

list_=list(type_)
print(list_)
print(type(list_))


# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Specify negative indexes if you want to start the search from the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# Update the tuple
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

