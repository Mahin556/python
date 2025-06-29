import os

print(os.system("df -h"))
print(os.system("systeminfo"))
print(os.system("wmic cpu list /format:list"))
print(os.system("free -h"))