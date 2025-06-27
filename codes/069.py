with open("demo1.txt","r") as rf:
    with open("demo2.txt","w") as wf:
        wf.write(rf.read())
    