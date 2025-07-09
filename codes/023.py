"""
There are four collection data types in the Python programming language:

-> List is a collection which is ordered and changeable. Allows duplicate members.
-> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-> Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

l1=["mahin","apple","mahin",22,5.11,True,None]
print(type(l1))

#list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

l2=["demo","hi"]
print(l1)
print(l1[1])
print(l1[1:5])
l1[1]="orange"
print(l1)
print(l1[1])


print(len(l1))

# l1.sort()
print(l1)

#
l1.reverse()
print(l1)

#
l1.append(45)
print(l1)

#
pop_item=l1.pop(3)
print(pop_item)

#
l1.insert(3,44)
print(l1)

#
l1.remove("mahin")
print(l1)

#
l1.extend(l2)
print(l1)

#
l1.append(l2)
print(l1)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Change a Range of Item Values
a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[1:3] = ["b", "w"]
print(a)
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
print([x for x in thislist])


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
newlist1 = []

for i in fruits:
  if "a" in i:
    newlist.append(i)
  if "a" == i[0]:
    newlist1.append(i)

print(newlist)
print(newlist1)

print([i for i in fruits if "a" in i])
print([i for i in fruits if "a" == i[0]])

# The Syntax
# newlist = [expression for item in iterable if condition == True]

#Only accept items that are not "apple":
print([x for x in fruits if "a" not in x])


newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x > 5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x.upper() for x in fruits]
print(newlist)

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print(sorted(thislist)) # only print in sorted order not change the list

# list.clear()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

thislist.pop() #by defautl delete last element

## Join(concatinate) two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


list1 = ["a", "b" , "c"]
if "a" in list1:
  print("present")
else:
  print("not present")

print(list1.count("a"))



fruits1 = ['orange', 'apple', 'pear']
fruits3 = [ 'orange', 'apple', 'pear']
fruits2 = ['banana', 'kiwi', 'apple', 'banana']
print(fruits1 == fruits3) # values are same
print(fruits1 is fruits3)

# string ---> list
list1=['orange', 'apple', 'pear']
list2=['banana', 'kiwi', 'apple', 'banana']
string="mahin 30"
newlist=string.split()
print(type(newlist))
print(newlist)
name,num=newlist
print(name," ",num)

#list ---> string
list1=['orange', 'apple', 'pear']
print(" ".join(list1))

list1=[[1,2,3,],[4,5,6],[7,8,9]]
for sublist in list1:
  for i in sublist:
    print(i)

print(list1[0][1])

list2=list(range(0,10))
print(list2)

print(list2.index(1)) # give 1 item index
print(list2.index(1)) # give 1 item index and start search after 3 index


list2=list(range(0,10))

def negativeList(list_name):
  return [ -x for x in list_name]

print(negativeList(list2))

list2=list(range(0,10))
def square(l):
    list1=[]
    for i in l:
      list1.append(i**2)
    return list1

print(square(list2))


list2=list(range(0,10))
def reverse(l):
    list1=[]
    for i in range(0,len(l)):
      item=l.pop()
      list1.append(item)
    return list1

print(reverse(list2))


list1=['orange', 'apple', 'pear']
def reverse_str(l):
  list1=[]
  for i in l:
    list1.append(i[-1::-1])
  return list1
print(reverse_str(list1))


list2=list(range(1,11))

def odd_even(l):
  odd=[]
  even=[]
  combo=[]
  for i in l:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i) 
  combo=[odd,even]
  return combo

print(odd_even(list2))

list1=[1,2,3,4]
list2=[2,3,5,6]
def common(l1,l2):
  common=[]
  for i in list1:
    if i in list2:
      common.append(i)
  return common

print(common(list1,list2))

list_=[13,43,55]
print(min(list_))
print(max(list_))

def greater_diff(l):
  return max(l) - min(l)

print(greater_diff(list_))
      
    
list_=[1,2,[3,4],[5,6]]
def no_of_list(l):
  no_of_list=0
  for i in l:
    if type(i) == list:
      no_of_list+=1
  return no_of_list

a = ["cat", "dog", "tiger"]
print(a.index("dog"))

a = [10, 20, 30, 40, 50, 40, 60, 40, 70]
res = a.index(40, 4, 8)
print(res)

a = ['red', 'green', 'blue']
try:
    index = a.index('yellow')
    print(a)
except ValueError:
    print("Not Present")

a = [("Alice", 21), ("Bob", 22), ("Charlie", 20), ("Bob", 24)]
res = a.index(("Bob", 22))
print(res)
print(no_of_list(list_))


a = [1, 4, 5, 6, 7]
for i, v in enumerate(a):
    print(i, v)

a = [1, 4, 5, 6, 7]

for i, v in enumerate(a):
    print(i, v)

a = [1, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd', 'e']
for i, v in zip(range(len(a)), zip(a,b)):
    print(i, v)
"""
0 (1, 'a')
1 (4, 'b')
2 (5, 'c')
3 (6, 'd')
4 (7, 'e')
"""

a = [1, 4, 5, 6, 7]
print([(i, a[i]) for i in range(len(a))])
