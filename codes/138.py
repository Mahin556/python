import sys

# Accepting the command line arguments

print(sys.argv[0]) # script name
print(sys.argv[1]) # first argument
print(sys.argv[2]) # second argument


# by default argv are string
print(type(sys.argv[1]))
print(type(int(sys.argv[1])))
print(type(float(sys.argv[1])))
