a=1
b=2
print(a+b)

c=5
d=2
print(c%d)

name="mahin"
print(name*5)

e=input("Enter any number:")
print(type(e))

# a=34
# b=80
A=int(input("Enter a variable A value: "))
B=int(input("Enter B variable A value: "))
if A>B:
    print(f"{A} is Greaterthen {B}")
else:
    print(f"{B} is Greaterthen {A}")

avg=(A+B)/2
print(avg)

i=0
for num in range(1,11):
    print(f"{num} + {i} --->",end="")
    i=num+i
    print(f"{i}")

sum_=sum(range(A,B))
print(f"The average of numbers between {A} to {B} --> {sum_/2}")
