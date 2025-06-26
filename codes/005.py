a=2+1
b=3-1
b+=2
b-=1

#   +	 Addition	      x + y	
#   -	 Subtraction	  x - y	
#   *	 Multiplication	  x * y	
#   /	 Division	      x / y	
#   %	 Modulus	      x % y	
#   **	 Exponentiation	  x **
#   //	 Floor division	  x // y


print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#   =	    x = 5	        x = 5	
#   +=	    x += 3	        x = x + 3	
#   -=	    x -= 3	        x = x - 3	
#   *=	    x *= 3	        x = x * 3	
#   /=	    x /= 3	        x = x / 3	
#   %=	    x %= 3	        x = x % 3	
#   //=	    x //= 3	        x = x // 3	
#   **=	    x **= 3	        x = x ** 3	
#   &=	    x &= 3	        x = x & 3	
#   |=	    x |= 3	        x = x | 3	
#   ^=	    x ^= 3	        x = x ^ 3	
#   >>=	    x >>= 3	        x = x >> 3	
#   <<=	    x <<= 3	        x = x << 3	
#   :=	    print(x := 3)	x = 3 print(x)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#or
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

# type casting
print(type(b))
b=str(b)
print(type(b))


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))
print(type(z))


x = "John"
# is the same as
x = 'John'
print("hello 'hi' ")

a = 4
A = "Sally"
print(a,A)
#A will not overwrite a


# Many Values to Multiple Variables
x,y,z=1,2,3
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
a,b,c=[1,2,3]
print(a)
print(b)
print(c)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

w = 1
x = "Python"
y = "is"
z = "awesome"
print(w, x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# print(w + x + y + z) #error

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)


# Global Variables

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# Local variable
b = "awesome"
def func():
  b="demo"
  print(b)

print(b)
func()
print(b)

# The global Keyword
def myfunc1():
  global x
  x = "fantastic"
myfunc1()
print("Python is " + x)

# use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Identity Operators
# if they are actually the same object, with the same memory location:
# is 	        Returns True if both variables are the same object	        x is y	
# is not	    Returns True if both variables are not the same object	    x is not y


# Membership Operators
# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y


#Bitwise Operators
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


print(6 & 3) #2
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 3) #7
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


#Operator Precedence

#   ()	                                            Parentheses	
#   **	                                            Exponentiation	
#   +x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
#   *  /  //  %	                                    Multiplication, division, floor division, and modulus	
#   +  -	                                        Addition and subtraction	
#   <<  >>	                                        Bitwise left and right shifts	
#   &	                                            Bitwise AND	
#   ^	                                            Bitwise XOR	
#   |	                                            Bitwise OR	
#   ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
#   not	                                            Logical NOT	
#   and	                                            AND	
#   or	                                            OR