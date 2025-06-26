#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace 
a = " Hello, World! "
print(a.strip()) #---> from the beginning or the end
print(a.rstrip()) #---> from the end
print(a.lstrip()) #---> from the beginning

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))   # H --> J

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
a = "Hello,World!,How,Are,You?"
print(a.split(","))


#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


