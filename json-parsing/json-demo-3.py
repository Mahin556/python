import json
import requests


data = requests.get('http://jsonplaceholder.typicode.com/todos/1')

if data.status_code==200:
    # print("Get successfull")
    content=data.json()
    print(content)
    print(content['userId'])
    for key,value in content.items():
        print(f"{key}:{value}")


# filtering based on email sufix
data1 = requests.get('https://jsonplaceholder.typicode.com/comments')
if data1.status_code==200:
    # print("Get successfull")
    content1=data1.json()
    print(len(content1))
    # print(content['userId'])
    # for key,value in content.items():
    #     print(f"{key}:{value}")
    objects=[]
    for item in content1:
        if item['email'].endswith("@juwan.us"):
            objects.append(item)
    print(objects)

    # listing all emails
    emails=[]
    for item in content1:
        emails.append(item['email'])
    print(emails)

    #printing all the emails into file
    emails=[]
    if content1:
        with open('email.txt',"a") as f:
             for item in content1:
                f.write(item['email']+"\n")
            
# requests.put('https://jsonplaceholder.typicode.com/posts')
