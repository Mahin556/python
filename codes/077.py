with open("poem.txt","r") as f:
    poem=f.read()
    if "Twinkle" in poem:
        print("Twinkle present")
    else:
        print("Twinkle not present")