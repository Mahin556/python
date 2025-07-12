import requests

responce=requests.get(" https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(responce.status_code)

content=responce.json()

print(content[0]["id"])

for i in range(len(content)):
    print(content[i]["id"])

for i in range(len(content)):
    print(content[i]["user"]["login"])
