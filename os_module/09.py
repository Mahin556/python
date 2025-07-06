import os

file_name="DEMO.txt"
file=open(file_name,"w")
file.write("Hello, How Are You?")
file.close()

file=open(file_name)
content=file.read()
print(content)
file.close()