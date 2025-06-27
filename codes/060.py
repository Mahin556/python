# syntax
# lambda arguments : expression

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

def add(a, b):
    return a + b

add2 = lambda a, b: a + b
print(add2(2, 3))

multiply = lambda a, b: a * b
print(multiply(2, 3))
print(add(5))  # ⚠️ Error: Missing second argument


# lambda expression practice
def is_even(a):
    return a % 2 == 0  # True if even, False otherwise
print(is_even(5))

iseven2 = lambda a: a % 2 == 0
print(iseven2(6))



last_char = lambda s: s[-1]
print(last_char('harshit'))


# lambda with if , else
def func(s):
    if len(s) > 5:
        return True
    return False

func = lambda s: True if len(s) > 5 else False

# lambda with if , else
def func(s):
    return len(s) > 5

func = lambda s: len(s) > 5
print(func('abcdefg'))


# Use that function definition to make a function that always doubles the number you send in:
# Example

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))