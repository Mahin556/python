class Persion:
    count_instance = 0
    def __init__(self, first_name, last_name, age): 
        Persion.count_instance += 1 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',') 
        return cls(first, last, age)

    @classmethod
    def count_instances (cls):
        return f"You have created {cls.count_instance} of Person class"

p1=Persion ('Harshit', 'Vashisth', 24) 
p2=Persion ('Harshit', 'Vashisth', 24)
print(Persion.count_instance)
print(p1.count_instance)

# p3=Persion('Mahin,Raza,22') error
p3=Persion.from_string('Mahin,Raza,22')
print(p3.first_name)
# from_string--->p3--->__init__
