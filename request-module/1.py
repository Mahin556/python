#https://www.w3schools.com/python/module_requests.asp
#https://www.geeksforgeeks.org/python/python-requests-tutorial/
#https://medium.com/@DoneWithWork/mastering-http-requests-with-pythons-requests-module-an-intermediate-guide-9c54ee173768
#pip install request

import requests
response = requests.get("https://api.github.com/users/octocat")
print(response.json()) # Access JSON response data

payload = {"key": "value"}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text) # Access text response



