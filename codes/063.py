# Only print one time because of curser moment
with open("demo1.txt","r") as f:
    print(f.read())
    print(f.read())

# need to wite 2time to read file twice
with open("demo1.txt","r") as f:
    print(f.read())

with open("demo1.txt","r") as f:
    print(f.read())