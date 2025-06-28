class student:
    language="python"  # Class attribute
    salary=1300000

    def __init__(self,name,language,salary): # dunder methord which is automatically called when object is created
       self.name=name
       self.language=language
       self.salary=salary
       print("__init__ method called")

    def getInfo(self):
       print(f"-> {self.name}\n-> {self.language}\n-> {self.salary}")
    
    @staticmethod #decorator
    def greet():
       print(f"hello")

demo1=student("Mahin","Python",1200000)
print(demo1.name,demo1.language,demo1.salary)
demo1.getInfo()
demo1.greet()


# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Example
# Create a class named Person, use the __init__() function to assign values for name and age:
#  The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:

# Example
# Insert a function that prints a greeting, and execute it on the p1 object:
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
# Example
# Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()


# Modify Object Properties
# You can modify properties on objects like this:
# Example
# Set the age of p1 to 40:
p1.age = 40


# Delete Object Properties
# You can delete properties on objects by using the del keyword:
# Example
# Delete the age property from the p1 object:
del p1.age

# Delete Objects
# You can delete objects by using the del keyword:
# Example
# Delete the p1 object:
del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
# Example
class Person:
  pass

