import os
parent_path="C:\\Users\\ADMIN\\Downloads\\hello"
dir="demo_789"
path=os.path.join(parent_path,dir)
os.rmdir(path)

# only remove empty directory

