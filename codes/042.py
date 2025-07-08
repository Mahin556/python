n=input("Enter a number: ")
sum=0
i=0
while i<len(n):
    sum+=int(n[i])
    i+=1

print(sum)

for i in range(100,0,-10):
   print(i)


password = ''

while password != 'password':
    print('What is the password?')
    password = input()