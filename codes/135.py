import re

text = "The quick brown fox"
pattern = r"The"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# find at start

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
    