def is_palendrom(word):
    reverse=word[-1::-1]
    if reverse==word:
        return "word is palendrom"
    
def is_palendrom(word):
    return word==word[-1::-1]

print(is_palendrom("madam"))
print(is_palendrom("mahin"))


# scope
x = 5 # global variable
def func(): 
    global x
    x = 7 # local variables
    return x
print(x)
print(func())
print(x)