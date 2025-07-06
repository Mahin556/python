import os

a = "hello/new.txt" # Relative path
b = os.path.abspath(a)    # Get absolute path

print(b)

#  we are using the os.path.abspath() function to get the absolute path of the current script file.

p = os.path.abspath(__file__)   # Get absolute path
print(p)

# __file__ attribute represents the script's relative path and os.path.abspath() converts it to the full absolute path by combining it with the current working directory.

f, n = "hello", "new.txt"  # Folder and file
a = os.path.abspath(os.path.join(f, n))  # Absolute path
print(a)