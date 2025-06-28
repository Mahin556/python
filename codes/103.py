class Laptop:
    Discount=20
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand=brand
        self.name=model_name
        self.price=price
        self.laptop_name = brand + model_name
    def discount(self,discount):
        return self.price-self.price*(discount/100)

Laptop.Discount=30

laptop1 = Laptop('hp','au114tx',3000)
print(laptop1.brand)
print(laptop1.discount(10))
print(laptop1.__dict__)