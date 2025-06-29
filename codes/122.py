# Enumerator

# Without enumerator function
names=["mahin","raza","john"]
pos=0
for name in names:
    print(f"{pos}--->{name}")
    pos+=1

# With enumerator function
for pos,name in enumerate(names):
    print(f"{pos}--->{name}")
    