# List comprehension
squares=[]

def square():
    for i in range(1,11):
        squares.append(i**2)
# square()
# print(squares)

square2=[x**2 for x in range(1,11)]
print(square2)

neg=[-x for x in range(1,11)]
print(neg)

names=["Mahin","harry","Raza"]

first_char=[x[0] for x in names]
print(first_char)

reverse_name=[name[-1::-1] for name in names]
print(reverse_name)

num=list(range(1,11))
print(num)
even_num=[i for i in num if i%2==0 ]
odd_num=[i for i in num if i%2!=0 ]
print(even_num)
print(odd_num)


list_=[True,"mahin",[1,2,3],1,2,3.0]
numbers=[str(i) for i in list_ if (type(i)==int or type(i)==float)]
print(numbers)
print(type(numbers[0]))

new_list=[ i*2  if i%2==0 else -i for i in num]
print(new_list)

nested_list=[[i for i in range(1,4)] for i in range(1,4)]
print(nested_list)