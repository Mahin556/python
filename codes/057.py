# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print(kid)
  print(type(kid))
my_function(fname = "Tobias", lname = "Refsnes")
# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

def my_function_2(**kid):
  for key,value in kid.items():
    print(key,value)
my_function_2(fname = "Tobias", lname = "Refsnes")

def my_function_3(name,**kid):
  for key,value in kid.items():
    print(key,value)
my_function_3("mahin",fname = "Tobias", lname = "Refsnes")



# dictionary unpacking
d= {'name': 'Harshit', 'age': 24}
my_function(**d)