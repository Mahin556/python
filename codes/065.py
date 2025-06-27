# readline method
with open("demo1.txt","r") as f:
    print(f"Curser position:- {f.tell()}")
    print(f.readline())
    print(f"Curser position:- {f.tell()}")
    print(f.readline())
    print(f"Curser position:- {f.tell()}")


# readlines
with open("demo1.txt","r") as f:
    print(f"Curser position:- {f.tell()}")
    print(f.readlines())
    f.seek(0)
    print(len(f.readlines()))
  
 