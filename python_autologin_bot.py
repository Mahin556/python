from selenium import webdriver  
import os

def startBot(username, password, url):
    path= "C:\Users\ADMIN\Downloads\chromedriver-win64"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

     # opening the website  in chrome.
    driver.get(url)

# Driver Code
# Enter below your login credentials
username = "Enter your username"
password = "Enter your password"

# URL of the login page of site
# which you want to automate login.
url = "Enter the URL of login page of website"

# Call the function
startBot(username, password, url)