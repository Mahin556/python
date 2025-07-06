import os

path="C:\\Users\\ADMIN\\Downloads"
file="file1.txt"
os.chdir(path)

f=open(file,"w")
f.close()

file_path=os.path.join(path,file)
os.remove(file_path)


# remove file not directory
