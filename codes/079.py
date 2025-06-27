import os

if os.path.exists("./tables"):
    pass
else:
    os.mkdir("./tables")

def tables():
    for i in range(1,21):
        with open(f"./tables/table_of_{i}.txt","a") as f:
          f.write(f"Table of {i}\n----------\n")
          for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")
        
tables()