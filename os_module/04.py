import os

print(os.listdir())  # list current directory

path="C:\\Users\\ADMIN\\Downloads"
dir_list=os.listdir(path)
for i in os.listdir(path):
    print(i)
print(len(dir_list))

#give list 