import os

path="C:\\Users\\ADMIN\\Downloads\\hello"
old_file="demo.txt"
old_file_path=os.path.join(path,old_file)
new_file="new.txt"
new_file_path=os.path.join(path,new_file)
os.rename(old_file_path,new_file_path)