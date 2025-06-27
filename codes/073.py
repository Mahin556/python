# reading a big file
with open('file.txt', 'r') as f:
  data = f.read(100)
  while len(data) > 0: 
    print(data)
    data = f.read(100)