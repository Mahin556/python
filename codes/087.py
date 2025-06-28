# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code

# A class defines what an object should look like, and an object is created based on that class. For example:
# Class	  Objects
# Fruit	  Apple, Banana, Mango
# Car	  Volvo, Audi, Toyota

# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


class student:
    language="python"  # Class attribute
    salary=1300000

    def getInfo(self):
       print(f"-> {self.name}\n-> {self.language}\n-> {self.salary}")
    
    @staticmethod #decorator
    def greet():
       print(f"hello")

demo1=student()
demo1.name="Rohan"  # Instance attribute
print(demo1.name,demo1.language,demo1.salary)
demo1.getInfo()
demo1.greet()

demo2=student()
demo2.name="Charles"  # Instance attribute
demo2.language="Javascript"
print(demo2.name,demo2.language,demo2.salary)

# name is object attribute and language,salary are class attributes as they are directly belong to the class
#we can use any thing in place of self but self is more discriptive
# Priority
# Instance attribute > Class Attribute


class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)