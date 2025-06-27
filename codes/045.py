import datetime
def avg():
    num1=int(input("Enter a number1: "))
    num2=int(input("Enter a number2: "))
    num3=int(input("Enter a number3: "))
    avg=(num1+num2+num3)/3
    return avg

def greet(date,msg="Hello"):
    print(msg,date)

print(avg())
print("hello")
# avg()
# avg()
# avg()
greet(datetime.datetime.now(),"How are you?")
greet(datetime.datetime.now())


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

