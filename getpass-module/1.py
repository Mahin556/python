import getpass
try:
    username = getpass.getuser()
    password = getpass.getpass(prompt=f'Enter password for {username}: ')
    print(f"Password entered for {username} (hidden): {password}")
except Exception as e:
    print(f"Error: {e}")

#https://www.geeksforgeeks.org/python/getpass-and-getuser-in-python-password-without-echo/
#https://www.geeksforgeeks.org/python/python-getpass-module/
