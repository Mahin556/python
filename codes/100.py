# OPERATOR OVERLOADING IN PYTHON
# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in Python can be overloaded using the following methods:
# nginx
# Copy
# Edit
# p1 + p2  # p1.__add__(p2)  
# p1 - p2  # p1.__sub__(p2)  
# p1 * p2  # p1.__mul__(p2)  
# p1 / p2  # p1.__truediv__(p2)  
# p1 // p2 # p1.__floordiv__(p2)

# __str__()  # used to set what gets displayed upon calling str(obj)

class Number:
  def __init__(self, n): 
    self.n = n
  def __add__(self, num): 
    return self.n + num.n

n = Number(1)
m = Number(2)
print(n + m)