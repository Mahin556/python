name=input("Name: ")
counted=[]
for i in name:
    if i.lower() not in counted:
        print(f"{i} ---> {name.lower().count(i.lower())}")
        counted.append(i.lower())
    
