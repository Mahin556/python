# @property decorator
class Employee:
    Company="ITC"
    def __init__(self):
        print("Employee constructor")
    def getInfo(self):
        print(f"Company is {self.Company} ")
    
    @property
    def name(self):
        return f"{self.fname},{self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
    
obj1=Employee()
obj1.name="Mahin raza"
print(obj1.fname)
print(obj1.lname)
print(obj1.name)

# Abstraction and Encapsulation

