# We can pass a 2 type of arguments in function
# 1. positional
# 2. Key:value(keyword)

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
# Example

def my_function(x, /):
  print(x)
my_function(3)
# But when adding the , / you will get an error if you try to send a keyword argument:

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
# Example
def my_function(x):
  print(x)
my_function(x = 3)


# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3)
# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:


# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
# Example
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)


