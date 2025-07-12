def decorator_function(any_function):
    def wrapper_function():
        print("This is wrapper function")
        any_function()
    return wrapper_function

@decorator_function
def func1():
    print("This is function1")

def func2():
    print("This is function2")

func1 = decorator_function(func1)
func1()