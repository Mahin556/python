with open("this_copy.txt") as f:
    content2 = f.read()

with open("this_copy1.txt") as f:
    content1 = f.read()


if content1 == content2:
    print("Yes these files are identical")
