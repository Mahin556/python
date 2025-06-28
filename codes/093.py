# Multile Inheritence
class Employee:
    Company="ITC"
    def getInfo(self):
        print(f"The name of the Employee is {self.name} and it's company is {self.Company} ")
    
class Coder:
    language="python"
    def LangInfo(self):
        print(f"The name of the Employee is {self.name} and it's favorite language is {self.language} ")

class Programmer(Employee,Coder):
    Company="ITC-Info"
    def __init__(self,name,language):
        self.name=name
        self.language=language
    

obj1=Programmer("Mahin","C++")
print(obj1.name)
obj1.getInfo()
obj1.LangInfo()

