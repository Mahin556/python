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
