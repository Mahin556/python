import json
import os
scrypt_path=os.path.dirname(__file__)
scrypt_absolute_path=os.path.join(scrypt_path,'file.json')


json_ = json.loads(open('./file.json').read())
value = json_['name']
print(value)

for key in json_:
    print(f"{key}==>{json_[key]}")
print()
print("#"*30)
print()
for key,value in json_.items():
    print(f"{key}==>{value}")
print()
print("#"*30)
print()
for key,value in json_.items():
    print("{}==>{}".format(key,value))