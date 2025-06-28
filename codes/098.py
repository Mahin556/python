class Employee:
    Company="ITC"
    
    @classmethod
    def getInfo(cls):
        print(f"company is {cls.Company} ")

print(Employee.Company)
obj1=Employee()
obj1.Company="ITC-Info"
print(obj1.Company)
obj1.getInfo()