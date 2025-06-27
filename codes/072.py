# read a file with emoji in win

with open('love_story.txt', 'r', encoding='utf-8') as f:
  print(f.encoding)
  data = f.read() 
  print(data)