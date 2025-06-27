# # Python has several functions for creating, reading, updating, and deleting files.
# # File Handling
# # The key function for working with files in Python is the open() function.

# # The open() function takes two parameters; filename, and mode.

# # There are four different methods (modes) for opening a file:

# # "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# # "a" - Append - Opens a file for appending, creates the file if it does not exist

# # "w" - Write - Opens a file for writing, creates the file if it does not exist

# # "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode(default)

# "b" - Binary - Binary mode (e.g. images)


# To open a file for reading it is enough to specify the name of the file:
f = open("file1.txt")
f = open("demofile.txt", "rt")
# Make sure the file exists, or else you will get an error.

# Reading a file
# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt")
print(f.read())
# Open a file on a different location:
f = open("D:\\myfiles\welcome.txt")
print(f.read())

# Close the file when you are finished with it:
f = open("demofile.txt")
print(f.readline())
f.close()
# You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.


# Using the with statement
with open("demofile.txt") as f:
  print(f.read())
# Then you do not have to worry about closing your files, the with statement takes care of that.

# Return the 5 first characters of the file: defult ---> whole file
with open("demofile.txt") as f:
  print(f.read(5))


# Read one line of the file:
with open("demofile.txt") as f:
  print(f.readline())

# Read two lines of the file:
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

# return line in form of list
with open("demo1.txt","r") as f:
    print(f.readlines())

# Loop through the file line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)

st="string"
with open("demofile.txt") as f:
  f.write(st)

# Open the file "demofile.txt" and append content to the file:
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

# Open the file "demofile.txt" and overwrite the content:
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())



# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

# Example

f = open("myfile.txt", "x") #---> a new empty file is created.


import os
# Remove the file "demofile.txt":
os.remove("demofile.txt")

# Check if file exists, then delete it:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Remove the folder "myfolder": You can only remove empty folders.
os.rmdir("myfolder")


#open the file
text_file = open('/Users/pankaj/abc.txt','r')
#get the list of line
line_list = text_file.readlines();
#for each line from the list, print the line
for line in line_list:
    print(line)
text_file.close() #don't forget to close the file


#open the file
text_file = open('/Users/pankaj/file.txt','w')
#initialize an empty list
word_list= []
#iterate 4 times
for i in range (1, 5):
    print("Please enter data: ")
    line = input() #take input
    word_list.append(line + '\n') #append to the list
text_file.writelines(word_list) #write 4 words to the file
text_file.close() #don’t forget to close the file


try:
  with open('log.txt', 'w') as f:
    print('Writing to log file...')
    f.write('Log entry started.\n')
    # Some error occurs
    result = 10 / 0
    f.write('This line will not be written.\n')
except ZeroDivisionError:
  print('An error occurred, but the file was closed automatically!')