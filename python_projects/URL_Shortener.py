import pyshorteners

long_url = input("Enter a URL:- ")
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(long_url)
print(f"Shortened URL: {short_url}")