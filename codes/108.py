#scope

def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300 #accessiable to function inside this function by not for outside
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#  variable created outside of a function is global and can be used by anyone:
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300
myfunc()
print(x)


# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
# Example
# If you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())

