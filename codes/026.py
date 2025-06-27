# set data type
# unordered collection of unique items

s = {1,2,3,2}
s_= {1,2,3.0,"demo",True,False}
# Note: 
# The values True and 1 are considered the same value in sets, and are treated as duplicates.
# The values False and 0 are considered the same value in sets, and are treated as duplicates.

# 1.0 == 1
# only int float str
# unique unordered
# print(s[1])
l = [1,2,3,4,5,5,5,5,6,7,7,8]
# remove duplicate
s2 = set(1)
print(s2)
s.add(4)
print(s)
s.remove(4)
print(s)
s.discard(4)
print(s)
s3=s.copy()

#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
s3.pop()

#The clear() method empties the set:
s.clear(4)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error.




#Once a set is created, you cannot change its items, but you can add new items.

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# in keyword to check if item is present or not in set 
if 'a' in s:
    print("present")
else:
    print("not present")

# for loop
for item in s:
    print(item)

#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

s1 = {1,2,3,4} 
s2 = {3,4,5,6}
# union
# intersection
#{1,2,3,4,5,6}
# |
union_set = s1 | s2
print (union_set)


set1 = {1,2,3,4} 
set2 = {3,4,5,6}

print(set1.difference (set2)) # Output: {1, 2, 6}
# Using intersection() method 
print(set1.intersection (set2)) # Output: {3}
# Using union() method
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6}
# Using issubset() method
print({1, 2}.issubset(set1)) # Output: True
# Using issuperset() method
print(set1.issuperset({1, 2})) # Output: True


# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
myset = set1 | set2 | set3 |set4
print(myset)

# Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
#Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# Keep the items that exist in both set1, and set2:
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
set3 = set1 - set2
print(set3)
# The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2
print(set3)
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

