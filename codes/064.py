# tell ---> get curser position

with open("demo1.txt","r") as f:
    print(f"Curser position:- {f.tell()}")
    f.read()
    print(f"Curser position:- {f.tell()}")

# seek ---> change curser position

with open("demo1.txt","r") as f:
    print(f"Curser position:- {f.tell()}")
    print(f.read())
    f.seek(0)
    print(f"Curser position:- {f.tell()}")
    print(f.read())
    print(f"Curser position:- {f.tell()}")
