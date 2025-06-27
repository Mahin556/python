# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
# Arbitrary Arguments are often shortened to *args in Python documentations.

def total(a,b):
  return a+b

def total_1(*args):
  print(args)
  print(type(args))

def total_2(*nums):
  total=0
  for i in nums:
    total+=i
  return total

total(2,3)
total_1(2,3,4,5,6)

print(total_2(2,3,4,5,6))


def demo(num1,*args):
  pass
demo(2,3,4) # correct
demo() #error
demo(2) # correct

def demo1(*args):
  pass
demo(2,3,4) # correct
demo() #correct
demo(2) # correct

def demo2(num1,num2,*args):
  pass
demo(2,3,4) # correct
demo(2,3) # correct
demo() #error
demo(2) # error

def demo3(*args,num):
  pass
demo(2,3,4) # all arguments go to args

# Function define ---> parameter
# Function call ---> argument

def total_3(*nums):
  total=0
  for i in nums:
    total+=i
  return total

num=[1,2,3]
total_3(num) # ---> go as a list
total_3(*num) # ---> unpacked list


