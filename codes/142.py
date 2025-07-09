names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]
res = zip(names, scores)
print(list(res))
#The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. 
#Each tuple contains elements from the input iterables that are at the same position.

#When using iterables of different lengths, the zip() will only pair up to the shortest iterable.
names = ['Alice', 'Bob', 'Charlie']
scores = [88, 94]  
res = zip(names, scores)
print(list(res))
#OUTPUT----> [('Alice', 88), ('Bob', 94)]


#Unzipping data with zip()
a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
fruits, quantities = zip(*a)
print(f"Fruits: {fruits}")
print(f"Quantities: {quantities}")

#Unzipping data with zip()
d = {'name': 'Alice', 'age': 25, 'grade': 'A'}
keys = d.keys()
values = d.values()
res = zip(keys, values)
print(list(res))
