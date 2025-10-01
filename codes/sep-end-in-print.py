#User function Template for python3
a = input()
b = input()
separator = input()[0]

########### Write your code below ###############

# Print with space
print(a+" "+b)

# Print without newline at the end
print(a+" "+b,end="")


# Print with separator
print(a,b,sep=separator)

# Print without space
print(a,b,sep="")

########### Write your code above ###############

###############################################################################################################################################################

a = input()
n = int(input())
#code here
#Given two inputs that are stored in variables a and n, you need to print a, n times in a single line without space between them. Output must have a newline at the end.
"""
Input: a = "Hello", n = 5
Output: HelloHelloHelloHelloHello
Explanation: a is printed n=5 times in a single line without space between them.
"""
print(a*n,sep="",end="\n")

###############################################################################################################################################################

#User function Template for python3
a = input()
b = input()
c = input()
# Write your code below that prints a a times and b b times, seperated by c
"""
Given three inputs that are stored in the variables a, b, and c. You need to print a a times and b b times  in a single line separated by c.

Examples:

Input: a = 6, b = 4, c = &
Output: 666666&4444
Explanation: 6 printed 6 times and 4 printed 4 times seperated by c = &.
"""

print(a*int(a),b*int(b),sep=c)

###############################################################################################################################################################

#User function Template for python3
########### Write your code below ###############

# Take string input and print the string input

# Take integer input and add 10 to the integer input and print

# Take floating-point input and multiply the float input by 10 and print

########### Write your code above ###############
string=input()
print(string)

num=int(input())
print(num+10)

float_num=float(input())
print(float_num*10)

---

a=int(input())
b=int(input())
#code here
p = a and b
#Do a or b below
q = a or b
#Do not a below
r = not a
#The code below prints the output. Don't change it!
print(p,q,r)

---

a=int(input())
b=int(input())
c=int(input())
#code here
#Do a^a below
d=a^a
#Do c^b below
e=c^b
#Do a&b below
f=a&b
#Do c|(a^a) below
g=c|(a^a)
#Do ~e below
e=~e
print(d, e, f, g)

---
a = int(input())
b = int(input())

########### Write your code below ###############

# Write Code to Swap
a, b = b, a

########### Write your code above ###############

print(a, b)

---
a = int(input())
b = int(input())

########### Write your code below ###############

# Write Code to Swap
c=a
a=b
b=c

########### Write your code above ###############

print(a, b)

---
#User function Template for python3
a = int(input())
n = int(input())
r = 2
"""
Given three integers, a, r and n. Where a is the first term, r is the common ratio of a G.P. and r is equal to 2.  Calculate the nth term of GP.

The nth term is given by an = a * r(n-1), where r = 2.

Examples:

Input: a = 2, n = 10
Output: 1024
Explanation: an = a * rn-1 = 2 * 210-1 = 1024
"""

########### Write your code below ###############
# Compute the GP Term
ans = a * (r**(n-1)) 
########### Write your code above ###############

print(ans)

---

