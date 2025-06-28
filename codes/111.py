# Python Math

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:
# Example
x = abs(-7.25)
print(x)

# The pow(x, y) function returns the value of x to the power of y (xy).
# Example
# Re the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print(x)

# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:
import math

# The math.sqrt() method for example, returns the square root of a number:
# Example
import math
x = math.sqrt(64)
print(x)

# he math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
# Example
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1


# The math.pi constant, returns the value of PI (3.14...):
# Example
import math

x = math.pi

print(x)