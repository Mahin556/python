words = ["history","power","contestation"]


with open("demo_.txt","r",encoding="utf-8") as f:
    content=f.read()

for word in words:
  content=content.replace(word,"######")

with open("demo_.txt","w") as f:
    content=f.write(content)


 