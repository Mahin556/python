with open("log.txt", encoding="utf-8") as f:
    lines = f.readlines()

found = False
lineno = 1

for line in lines:
    if "python" in line.lower():  # optional: case-insensitive check
        print(f"Yes, 'python' is present. Line no: {lineno}")
        found = True
        break
    lineno += 1

if not found:
    print("No, 'python' is not present.")
