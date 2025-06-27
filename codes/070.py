with open("file1.txt","r") as rf:
    with open("file2.txt","w") as wf:
        for line in rf:
          wf.write(f"{line.split(",")[0]} salary is {line.split(",")[1]}")