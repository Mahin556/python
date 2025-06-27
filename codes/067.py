# f = open(r"G:\new_folder\file1.txt")
# f.close()
# \n, \t
# Windows     \
# Linux , mac - /

f=open("demo1.txt","r")
for line in f:
    print(line)

f.seek(0)
for line in f.readlines():
    print(line)

f.seek(0)
for line in f.readlines()[:1]:
    print(line)
