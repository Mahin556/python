class Employee:
    Company="ITC"
    def __init__(self):
        print("Employee constructor")
    def getInfo(self):
        print(f"The name of the Employee is {self.name} and it's company is {self.Company} ")
    
class Coder:
    language="python"
    Company="ITC-Info"
    def __init__(self):
        print("Coder constructor")
        super().__init__()
    def LangInfo(self):
        print(f"The name of the Employee is {self.name} and it's favorite language is {self.language} ")

class Programmer(Coder):
    def __init__(self,name,language):
        Coder.__init__(self)
        print("Programmer constructor")
        self.name=name
        self.language=language

obj1=Programmer("Mahin","C++")  