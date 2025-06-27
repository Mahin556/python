num=int(input("Enter a number: "))
#num --> 5
# 5*4*3*2*1
# factorial(n) ---> n * factorial(n-1)
def factorial_func(num):
    if (num==0 or num==1):
        return 1
    factorial=num*factorial_func(num-1)
    return factorial

# 5
# 5*4
# 5*4*3
# 5*4*3*2
# 5*4*3*2*1 

print(factorial_func(num))