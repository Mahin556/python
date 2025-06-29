#Iterator vs Iterable

numbers=[1,2,3,4] #, tuples, string

squares=map(lambda a:a**2,numbers) # iterator
print(next(squares))

# for i in numbers:
# print(i)
number_iter = iter (numbers)
print (next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
