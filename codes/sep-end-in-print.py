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

