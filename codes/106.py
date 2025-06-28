# # Python Iterators
# # An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# # Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# #Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# We can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
mystr = "banana"
for x in mystr:
  print(x)
# The for loop actually creates an iterator object and executes the next() method for each loop.

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


class Mynum:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj1=Mynum()
myiter=iter(obj1)
for i in myiter:
   print(i)
print()