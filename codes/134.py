import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
print(search)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


text = "The quick brown fox"
pattern = r"browr"

search = re.search(pattern, text)
print(search)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


# find all occurence and return a string
text = "The quick brown fox brown"
pattern = r"brown"

search = re.findall(pattern, text)
print(search)
