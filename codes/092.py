#Single Inheritence
class Employee:
    Company="ITC"
    def getInfo(self):
        print(f"The name of the Employee is {self.name} and it's company is {self.Company} ")
    
class Programmer(Employee):
    Company="ITC-Info"
    def __init__(self,name):
        self.name=name
    

obj1=Programmer("Mahin")
print(obj1.name)
obj1.getInfo()
