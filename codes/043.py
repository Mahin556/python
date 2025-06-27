name=input("Name: ")

counted=[]
i=0
while i<len(name):
    if name[i].lower() not in counted:
        print(f"{name[i]} ---> {name.lower().count(name[i].lower())}")
        counted.append(name[i].lower())
    i+=1
