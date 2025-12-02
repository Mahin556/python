```python
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(0)) # False
print(bool(1))
print(bool("")) # False
print(bool(not True)) # False
bool(None) # False
bool(()) # False
bool([]) # False
bool({}) # False


def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
```
---

```python
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
```

---

