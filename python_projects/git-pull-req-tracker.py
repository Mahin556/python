import requests

url='https://api.github.com/repos/EbookFoundation/free-programming-books/pulls'

response = requests.get(url)

if response.status_code == 200:
    pull_requests = response.json()
    pr_creators = {}
    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator]+=1
        else:
            pr_creators[creator]=1
        
    for creator,count in pr_creators.items():
        print(f"Creator: {creator}: {count} PRs")
    
else:
     print(f"Failed to make connection. Status Code: {response.status_code}")