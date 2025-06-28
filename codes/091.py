from random import randint

class Demo:
  a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute· is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # class attribute not changed



class Train:
  def book (self, trainNo, fro, to):
    print(f"Ticket is booked in train no: {trainNo} from {fro} to {to}")
  def getStatus(self, trainNo):
    print(f"Train no: {trainNo} is running on time")
  def getFare(self, trainNo, fro, to):
    print(f"Ticket fare in train no: {trainNo} from {fro} to {to} is {randint(222, 5555)}")

obj1=Train()
obj1.book(345,"delhi","mumbai")
obj1.getStatus(345)
obj1.getFare(345,"delhi","mumbai")