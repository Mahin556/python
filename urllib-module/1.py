#https://neuralpai.medium.com/working-with-pythons-urllib-library-a-beginner-s-guide-79bcad776a8e
#https://www.geeksforgeeks.org/python/python-urllib-module/
import urllib.request
url = 'https://example.com'
response = urllib.request.urlopen(url)
content = response.read()
content = content.decode('utf-8')
print(content)