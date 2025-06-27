with open("demo1.txt","r+") as f:
    f.write("Demo")

# start overwriting the content of file till the string end 
# give error if file not exist

with open("demo1.txt","r+") as f:
    f.seek(len(f.read()))
    f.write("Demo")

    