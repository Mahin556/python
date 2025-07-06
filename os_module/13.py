import os
# environ is not a function but a process parameter through which we can access environment variables of the system.

home=os.environ['HOME']
print(home)
print(os.environ.get("HOME"))

# this is the login of the user in
# the terminal that spawned this process.
print(os.getlogin())