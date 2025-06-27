l=[]
for i in range(1,9):
    l.append(int(input(f"Enter number{i}: ")))
s=set(l)
print(s)


s1=set()
for i in range(1,9):
    s1.add(int(input(f"Enter number{i}: ")))
print(s1)

s3=set()
s3.add(18)
s3.add("18")
print(s3)
