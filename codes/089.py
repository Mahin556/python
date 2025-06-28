class Employee:
    company="Microsoft"
    def __init__(self,name,pin,salary):
        self.name=name
        self.pin=pin
        self.salary=salary

    def EmployeeInfo(self):
        print(f"Employee:- {self.name}\nPin:- {self.pin}\nSalary:- {self.salary}")

employee1=Employee("mahin","3406","1200000")
print(employee1.name,employee1.pin,employee1.salary)
employee1.EmployeeInfo()