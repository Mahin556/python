import os
import os.path


print("### BY WHILE LOOP ###")
# To walk up a directory tree
current_directory = os.getcwd()
# print(current_directory)

# print(os.path.dirname(current_directory))
# print(os.path.basename(current_directory))

while os.path.basename(current_directory):
    current_directory = os.path.dirname(current_directory)
    print(current_directory)


print("### BY FOR LOOP ###")
current_directory = os.getcwd()

#os.sep is a constant provided by Python's os module that represents the character used by the operating system to separate pathname components. This character is platform-dependent, ensuring that code handling file paths can be written in a cross-platform compatible manner without needing to hardcode specific separators like / for Unix-like systems or `\` for Windows.
print(os.sep)
dirs=[]
for _ in range(current_directory.count(os.sep)):
    dirs.insert(0,current_directory)
    current_directory=os.path.dirname(current_directory)

for dir in dirs:
    print(dir)
