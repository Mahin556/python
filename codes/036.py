num=int(input("Enter a multiplication table number: "))
length=int(input("Enter a table lenght: "))

i=1
while i<=length:
    print(f"{num} * {i} = {num*i}")
    i+=1

