work="Donkey"

with open("demo.txt","r") as f:
    content=f.read()

newContent=content.replace('donkey',"######")

with open("demo.txt","w") as f:
    content=f.write(newContent)


 