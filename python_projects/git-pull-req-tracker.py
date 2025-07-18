import requests


def get_pull_info(url):
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

def main():
    acc_name = input("Enter You Account name:- ")
    repo_name = input("Enter You Repository name:- ")
    url=f"https://api.github.com/repos/{acc_name}/{repo_name}/pulls"
    get_pull_info(url)

if __name__ == '__main__':
    main()