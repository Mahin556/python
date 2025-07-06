def my_sum(*args):
    if all([(type(i)==int or type(i)==float) for i in args ]):
        sum=0
        for i in args:
            sum+=i
        return sum
    else:
        raise TypeError("Only integer or float values are allowed")

print(my_sum(1, 2, 3, 4, 8.9))
print(my_sum(1, 2, 3, 4, 8.9, 'harshit', ['harshit']))
