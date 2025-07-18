# https://www.geeksforgeeks.org/python/network-scanning-using-scapy-module-python/
# pip3 install scapy
import scapy.all as scapy
request = scapy.ARP()
print(request.show())
print(request.summary())

# References
# http://stackoverflow.com/questions/54576932/so-since-scapy-has-been-renamed-to-kamene-how-would-i-import-and-use-base64-byt
# https://www.freecodecamp.org/news/how-to-use-scapy-python-networking/

