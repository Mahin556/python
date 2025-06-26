import hashlib

def hash_file(FileName):
    hash=hashlib.sha256()
    with open(FileName, "rb") as file:
        chunk = 0
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            hash.update(chunk)
    return hash.hexdigest()

if __name__ == '__main__':
    msg1 = hash_file("file1")
    msg2 = hash_file("file2")
    if(msg1 != msg2):
        print("These files are not identical")
    else:
        print("These files are identical")


