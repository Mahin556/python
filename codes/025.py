marks={
    "mahin": 75,
    "raza": 50,
    "rohan": 35,
    0:"demo",
    1:2,
    "demo":["list1","list2"],
    1.0:3,
    "list":[],
}

user=dict(name="demo",age="22")
print(type(user))

print(marks)
print(marks["mahin"])
print(marks)
print(type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks["mahin"]=65
print(marks)
marks.update({"mahin":75}) # update
marks.update({"sunny":75}) # add
print(marks)
print(marks.get("mahin")) # give None if key does not exits
print(marks["mahin"]) # give error if key does not exits
marks1=marks.copy()

value=marks.pop("madhin",60)
print(value)

marks.clear()
print(marks)

if "name" in user:
    print("present")
else:
    print("not present")

if "name" in user.values():
    print("present")
else:
    print("not present")

    
for i in user: 
    print(user[i])


# How to add data to empty dictionary
user_info2={}
user_info2['name'] = 'mohit'
user_info2['age'] = 45
print (user_info2)



#items method
user_items= user_info2.items() 
print (user_items)
print(type (user_items)) #---> values types
# [('name', 'harshit'), ('age', 24), ('fav_movies', ['coco', 'kimi no na wa']),
for key, value in user_info2.items():
    print(f"key is {key} and value is {value}")



# pop method
popped_item = user_info2.pop('name') 
print(f"popped item is {popped_item}") 
print(user_info2)

#popitem method
popped_item = user_info2.popitem()
print(type(popped_item)) #---> tuple


user_info = {
'name': 'harshit',
'age': 24,
'fav_movies': ['coco', 'kimi no na wa'],
'fav_tunes': ['awakening', 'fairy tale'],
}
more_info ={'State':'Haryana', 'hobbies': ['coding', 'reading', 'guitar']}

user_info.update(more_info)
user_info.update({})  #---> does not delete data


# dict with multiple same values

# fromkeys
# d = {'name': 'unknown', 'age': 'unknown'} I
d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
print(d)
c=dict.fromkeys("abc","unknown")  #---> {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}
print(c)  

e=dict.fromkeys(range(1,11),"unknown")

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# he del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# The del keyword can also delete the dictionary completely:


if d.get('names'):
    print('present')
else:
    print('not present')
# if None ---> False else ---> True


user = {'name': 'Harshit', 'age': 24} 
print(user.get('fav', 'not found!'))

# two same key can exist in dict but last one overwrite 
def cube(n):
    cubes={}
    for i in n:
        cubes.update({i:i**2})
    return cubes

l=[1,2,3,4,5,6,7]
print(cube(l))


# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)


# ake a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
# ExampleGet your own Python Server
# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Print the name of child 2:
print(myfamily["child2"]["name"])

# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])

    