# Multile Inheritence
class Employee:
    Company="ITC"
    def getInfo(self):
        print(f"The name of the Employee is {self.name} and it's company is {self.Company} ")
    
class Coder(Employee):
    language="python"
    Company="ITC-Info"
    def LangInfo(self):
        print(f"The name of the Employee is {self.name} and it's favorite language is {self.language} ")

class Programmer(Coder):
    def __init__(self,name,language):
        self.name=name
        self.language=language
    

obj1=Programmer("Mahin","C++")
print(obj1.name)
obj1.getInfo()
obj1.LangInfo()


class class1:
    a=1
class class2(class1):
    b=2
class class3(class2):
    c=3

obj2=class1()
print(obj2.a)

obj3=class2()
print(obj3.a)
obj4=class2()
print(obj4.b)

obj5=class3()
print(obj5.a)
obj6=class3()
print(obj6.b)
obj7=class3()
print(obj7.c)