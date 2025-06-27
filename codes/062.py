# f=open("demo1.txt","x")

# f=open("demo1.txt","a")
# f.write("An astronaut throws a song quickly.\n")
# f.close()

with open("demo1.txt","r") as f:
    print(f.readlines())
print(f.closed)