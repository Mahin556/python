import os 
#importing os module

# Use os.path.exists for both files and directories:
result = os.path.exists("C:\\Users\\ADMIN\\Downloads\\hello") #giving the name of the file as a parameter.
print(result)

# Use os.path.isdir for directories only:
result=os.path.exists("C:\\Users\\ADMIN\\Downloads\\hello")
print(result)

if not os.path.isdir("directory_name"):
    os.mkdir("directory_name")
