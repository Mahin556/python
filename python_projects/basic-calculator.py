# Simple calculator in python

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

while True:
    # Input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == '+':
        print(f"Sum of {num1} and {num2} is: {add(num1, num2)}")
    elif operation == '-':
        print(f"Substraction of {num1} and {num2} is: {substract(num1, num2)}")
    elif operation == "*":
        print(f"Multiplication of {num1} and {num2} is: {multiply(num1, num2)}")
    elif operation == '/':
        print(f"Division of {num1} and {num2} is: {devide(num1, num2)}")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")

    is_continue = input("Do you want to perform another calculation? (yes/no)")
    if is_continue.lower() != 'yes':
        print("Exiting the calculator. Goodbye!\n")
        break

    



