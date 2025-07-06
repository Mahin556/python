import os

def current_dir():
    cwd=os.getcwd()
    print(cwd)

def dir_create(parent_dir,directory,mode=''):
    try:
        if mode=='':
            path=os.path.join(parent_dir,directory)
            os.mkdir(path)
        else:
            path=os.path.join(parent_dir,directory)
            os.mkdir(path,mode)
        return f"Directory {directory} Created"
    except:
        return f"Directory {path} already created"

for i in range(1,51):
    path = f"demo_{i}"
    print(dir_create("C:\\Users\\ADMIN\\Downloads",path))
 

# create a directory but not create parent dir