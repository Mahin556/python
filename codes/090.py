class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"Square of {self.n} is {self.n**2}")
    def cube(self):
        print(f"Cube of {self.n} is {self.n**3}")
    def root(self):
        print(f"Cube of {self.n} is {self.n**0.5}")

num1=calculator(5)
num1.cube()
num1.square()
num1.root()



