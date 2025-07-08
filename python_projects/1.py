import requests
from bs4 import BeautifulSoup

def get_data(url):
    text=requests.get(url)
    return text
    
url="https://covid.cdc.gov/covid-data-tracker/#maps_positivity-week"
text=get_data(url).text
soup = BeautifulSoup(text, "html.parser")
print(soup.title)
for link in soup.find_all('a'):
   print(link.get('href'))
