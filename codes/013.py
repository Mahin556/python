print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(0)) # False
print(bool(1))
print(bool("")) # False
print(bool(not True)) # False
bool(None) # False
bool(()) # False
bool([]) # False
bool({}) # False


def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))