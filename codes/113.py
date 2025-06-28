# Raising a error

def add(a,b):
    if (type(a)==int and type(b)==int):
        return a+b
    return "Not a valid data type"

print(add(2,3))
print(add("2","3"))


def add1(a,b):
    if (type(a)==int and type(b)==int):
        return a+b
    raise TypeError("Not a valid data type")
print(add1(2,3))
print(add1("2","3"))