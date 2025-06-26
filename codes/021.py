from datetime import datetime

name=input("Enter a name: ")
print(f"Good Afternoon {name}")


letter="""
Dear <Name>,
You are selected!
<|Date|>"""

name=input("Enter your name: ")
date=str(datetime.now())

print(letter.replace("<Name>",name).replace("<|Date|>",date))