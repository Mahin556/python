import json

with open('./file.json') as f:
    json_=json.load(f)

value = json_['name']
print(value)