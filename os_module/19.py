import os
# Path Representation in Python: Paths (binary or otherwise) are represented as strings.

# os.path Module: Provides many functions for handling string-based paths.

# Cross-Platform Compatibility: The os module, including os.path, adapts to the operating system (e.g., uses / on Unix and \ on Windows).

# Dynamic Path Creation: Programs can build OS-compatible paths dynamically.

# Common Path Methods: Frequently used os.path methods include split, basename, and dirname for splitting and joining paths.

# get the current working directory
current_directory = os.getcwd()

# split the leaf level of the path from the parent path
print(os.path.split(current_directory))
parent,child=os.path.split(current_directory)
print(parent)
print(child)
# ('C:\\Users\\ADMIN\\Downloads', 'python')

# returns the parent path
print(os.path.dirname(current_directory))
print(os.path.dirname(os.path.join(current_directory,"file1")))



# returns the leaf name
print(os.path.basename(current_directory))