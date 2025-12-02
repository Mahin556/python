```python
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

i=0
while i<len(a):
    print("demo:",a[i])
    i+=1

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```
```python
#Slicing
b = "Hello, World!"
print(b[2:5]) #---> llo

#Slice From the Start
b = "Hello, World!"
print(b[:5]) #---> Slice

#Slice To the End
b = "Hello, World!"
print(b[2:]) #---> llo, World!

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])  #---> orl
```
```python
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

print(a[-1::-1])

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

print(a.count("l"))


first_name, last_name=input("enter your Full name: ").split()
first_name, last_name=input("enter your Full name: ").split(",")
print(f"First name: {first_name}\nLastname: {last_name}")

# converts the first character to 
# upper case and rest to lower case 
text = 'geeKs For geEkS'
print("\nConverted String:")
print(text.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

s = "GeeksforGeeks"
res = s.startswith("for")
print(res)
# Parameters:
# prefix: A string or a tuple of strings to check at the start.
# start (optional): Index to start checking from.
# end (optional): Index to stop checking.
# Return Type: The method returns a Boolean:
# True if the string starts with the specified prefix.
# False if it does not.

#Start with 5th index
s = "GeeksforGeeks"
print(s.startswith("for", 5))

#find in between
s = "GeeksforGeeks"
print(s.startswith("for", 5, 8))

# Checking Multiple Prefixes
s = "GeeksforGeeks"
res = s.startswith(("Geeks", "F"))
print(res)
# We can also check if the string starts with any one of several prefixes by passing a tuple of prefixes.


a = ['Hello', 'world', 'from', 'Python']
res = ' '.join(a)
print(res)
#separator.join(iterable)

s = ("Learn", "to", "code")
# Separator "-" is used to join strings
res = "-".join(s)
print(res)

s = {'Python', 'is', 'fun'}
# Separator "-" is used to join strings
res = '-'.join(s)
print(res)

d = {'Geek': 1, 'for': 2, 'Geeks': 3}
# Separator "_" is used to join keys into a single string
res = '_'.join(d)
print(res)
# When using the join() method with a dictionary, it will only join the keys, not the values. This is because join() operates on iterables of strings and the default iteration over a dictionary returns its keys.

s = "hello"
res = s.islower()
print(res)

s2 = "Hello"
res2 = s2.islower() #false
print(res2)

s3 = "hello123"
res3 = s3.islower() #true
print(res3)

s4 = ""
res4 = s4.islower() #false
print(res4)

s5 = "123@"
res5 = s5.islower() #false
print(res5)


string = "123456789"
result = string.isnumeric()
print(result)

# Given string
string = '123geeks456for789geeks'
count = 0
new_string = ""
for ch in string:
    if ch.isnumeric():
        count += 1
    else:
        new_string += ch
print("Number of numeric characters:", count)
print("String after removing numeric characters:", new_string)

string = '123ayu456'
print(string.isnumeric()) #false

string = '123456'
print(string.isnumeric()) #true

# isnumeric() to check White-spaces
s = " "
p = "12 3"

print(s.isnumeric())  # False
print(p.isnumeric())  # False


string1 = '123'
string2 = '⅓'
string3 = '²'
string4 = '2167'  # 'Ⅷ'; ROMAN NUMERAL EIGHT

print(string1.isnumeric())  # True
print(string2.isnumeric())  # True
print(string3.isnumeric())  # True
print(string4.isnumeric())  # True


string = '75'
if string.isnumeric() and int(string) > 50:
    print("Valid Number")
else:
    print("Invalid Number")


# integer validation
number = 75
string = str(number)
result = string.isnumeric()
print(result)

# float validation
number = 5.65
string = str(number)
result = string.replace('.', '', 1).isnumeric()
print(result)


a = "12345"
print(a.isdigit())  # true

b = "1234a5"
print(b.isdigit()) #false

# Only digits
print("987654".isdigit()) #true

# Digits and alphabet
print("987b54".isdigit()) #false

# Empty string
print("".isdigit()) #flase

# Unicode for '1'
a = "\u0031"  
print(a.isdigit()) #true

# Devanagari digit for '1'
b = "\u0967"  
print(b.isdigit()) #true


print("I".isdigit())  #false
print("X".isdigit())  #false
print("VII".isdigit())  #false

a = "12345"
print(a.isdecimal())  # This will print True as all characters are digits

b = "12345a"
print(b.isdecimal())  # This will print False because 'a' is not a decimal character

e = "123.45"
print(e.isdecimal())  # False, because '.' is not a decimal character

f = "100,000"
print(f.isdecimal())  # False, because ',' is not a decimal character

d = "12 34"
print(d.isdecimal())  
# This will print False because there’s a space between the numbers

c = "١٢٣٤٥"  # Arabic-Indic numerals
print(c.isdecimal())  # True, because these characters are considered decimal in their script

d = "Ⅻ"  # Roman numeral for 12
print(d.isdecimal())  # False, Roman numerals are not decimal

g = "-12345"
print(g.isdecimal())  # False, because of the negative sign

h = "$12345"
print(h.isdecimal())  # False, because of the '$' symbol


s1 = "HelloWorld"
res1 = s1.isalpha() #true
print(res1)

s2 = "Hello123"
res2 = s2.isalpha() #true
print(res2)

s = "Hello World"
print(s.isalpha()) #false

s = "Python programming"
p = s.index("prog")
print(p)

s = "Python programming is fun"
p = s.index("is", 10, 25)
print(p)

a = "shakshi" # name 
b = 22 # age
msg = "My name is {0} and I am {1} years old.".format(a,b) #My name is shakshi and I am 22 years old.
print(msg)

# using a single placeholder
print("{}, a platform for coding enthusiasts.".format("GeeksforGeeks"))

# formatting with a variable
a = "Python"
print("This article is written in {}.".format(a))

# formatting with a number
b = 18
print("Hello, I am {} years old!".format(b))

#The number of placeholders must match the number of values provided.
# Using multiple placeholders
print("{} is a {} science portal for {}.".format("GeeksforGeeks", "computer", "geeks"))

# Formatting different data types
print("Hi! My name is {} and I am {} years old.".format("User", 19))

# Values replace placeholders in order
print("This is {} {} {} {}.".format("one", "two", "three", "four"))


#Positional and Keyword Arguments in format
# Positional arguments (placed in order)
print("{} love {}!!".format("GeeksforGeeks", "Geeks"))

# Changing order using index
print("{1} love {0}!!".format("GeeksforGeeks", "Geeks"))

# Default order in placeholders
print("Every {} should know the use of {} {} programming and {}".format("programmer", "Open", "Source", "Operating Systems"))

# Reordering using index
print("Every {3} should know the use of {2} {1} programming and {0}".format("programmer", "Open", "Source", "Operating Systems"))

# keyword arguments
print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg="GeeksforGeeks"))


#Formatting with Type Specifiers
product, brand, price, issue, effect = "Smartphone", "Amazon", 12000, "bug", "troubling"
print("{:<20} is a popular electronics brand.".format(brand))  
print("They have a {} for {} rupees.".format(product, price))  
print("I wondered why the program was {} me—turns out it was a {}.".format(effect, issue))  
print("Truncated product name: {:.5}".format(product))

"""Output
Amazon               is a popular electronics brand.
They have a Smartphone for 12000 rupees.
I wondered why the program was troubling me—turns out it was a bug.
Truncated product name: Smart
"""

"""Explanation:
%-20s left-aligns the brand name within 20 spaces.
%s inserts strings dynamically.
%d formats integers properly.
%.5 truncates the product name to the first 5 characters.
"""


print("This site is {:.6f}% securely {}!!".format(100, "encrypted"))
# To limit the precision
print("My average of this {} was {:.2f}%".format("semester", 78.234876))
# For no decimal places
print("My average of this {} was {:.0f}%".format("semester", 78.234876))
# Convert an integer to its binary or other bases
print("The {} of 100 is {:b}".format("binary", 100))
print("The {} of 100 is {:o}".format("octal", 100))

"""Output
This site is 100.000000% securely encrypted!!
My average of this semester was 78.23%
My average of this semester was 78%
The binary of 100 is 1100100
The octal of 100 is 144
Explanation:
"""
"""{0:f}: Floating-point representation.
{1:.2f}: Floating-point with two decimal places.
{1:.0f}: Rounds the floating number to the nearest integer.
{1:b}: Converts integer to binary.
{1:o}: Converts integer to octal.

%X hexadecimal uppercase 
%x hexadecimal lowercase
%e exponent notation
"""

print("The temperature today is {:.0f} degrees outside !".format(35.567))
#The temperature today is 36 degrees outside !

#dictionary unpacking
d = {"first_name": "Tony", "last_name": "Stark", "aka": "Iron Man"}
print("My name is {first_name} {last_name}, also known as {aka}.".format(**d))

s = "Welcome to GeekforGeeks!"
index = s.find("GeekforGeeks")
print(index)

s = "abc abc abc"
index = s.find("abc", 4)
print(index)

s = "Python is fun"
index = s.find("python")
print(index)
# Explanation: Since "python" (lowercase) does not match "Python" (uppercase), the method returns -1.
# No give error

# find() vs index()
# Both find() and index() methods locate a substring within a string. However, they differ in behavior when the substring is not found.

# find() returns the index or -1 if not found
# index() same as find(), but raises a ValueError if not found

s = "geeksforgeeks"
res = s.endswith("geeks")
print(res)  # This will print True because the string ends with 'geeks'

s = "geeksforgeeks"
res = s.endswith(("geeks", "com", "org"))
print(res)  # This will print True because 'geeks' is one of the options

s = "geeksforgeeks"
res = s.endswith("geeks", 5, 15)
print(res)  # This will print True because 'geeks' is found between position 5 and 15

f = "profile_picture.jpg"
if f.endswith((".jpg", ".png")):
    print("File is valid!")
else:
    print("Invalid file type!")

s = "Hello, World!"
# String encode() method in Python is used to convert a string into bytes using a specified encoding format. This method is beneficial when working with data that needs to be stored or transmitted in a specific encoding format, such as UTF-8, ASCII, or others.
encoded_text = s.encode()
print(encoded_text)

# We can encode a string by using utf-8 
a = "Python is fun!"
utf8_encoded = a.encode("utf-8")
print(utf8_encoded)

a = "Pythön"
encoded_ascii = a.encode("ascii", errors="replace")
print(encoded_ascii)

a = "Pythön"
encoded_xml = a.encode("ascii", errors="xmlcharrefreplace")
print(encoded_xml)

a = "Pythön"
encoded_backslash = a.encode("ascii", errors="backslashreplace")
print(encoded_backslash)



s = "hello world"
res = s.count("o")
print(res)

s = "Python is fun and Python is powerful."
print(s.count("Python"))

s = "apple banana apple grape apple"
substring = "apple"
# Using start and end parameters to count occurrences 
# of "apple" within a specific range
res = s.count(substring, 1, 20)  
print(res)




s1 = "hello"
s2 = s1.center(20)
print(s2)

a = "hello"
b = a.center(20, '-')
print(b)

a = "hello"
b = a.center(3)
print(b)

h1 = "Name"
h2 = "Age"
h3 = "Location"

s1 = h1.center(20, '-')
s2 = h2.center(20, '-')
s3 = h3.center(20, '-')

print(s1)
print(s2)
print(s3)



txt = "36 is my age."
x = txt.capitalize()
print (x)
#output 36 is my age.


myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))
```
```python
#String Format

age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# Escape Characters
# \'	Single Quote	
# \""	Double Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# \ooo	Octal Value	print("\141")	a
# \xhh	Hex Value	print("\x61")	a
# \r	Carriage Return	print("12345\rAB")	AB345

#"\r" moves the cursor to the beginning of the current line — but does not go to the next line. So, anything you write after \r will overwrite from the beginning of the same line.

print("12345\rAB")
#Output:
#AB345
```
```bash
# String is Immutable
name="Mahin raza"

print(name[0:6])
print(name[:6])

print(name[6:10])
print(name[6:])
print(name[:])
print(name[1:5])

# name=name.replace("n","r",1)
# print(name)

# name=name.upper()
print(name.upper())
print(name)

print(name.endswith("raza"))
print(name.startswith("m"))
print(name.capitalize())
print(name.title())
print(name[::2])
```
```python
#Raw Strings
print(r"line1\nline2")
```
```python
#Emoji
print("\U0001f600")
```
```python
print(round(2**0.5,4))
print(round(1.003140,4))
```