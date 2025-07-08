import sys
import pyjokes

print(sys.version) #python interpreter version

print("Printing joke.....")
joke=pyjokes.get_joke()
print(joke)

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')
print("Exit")

sys.stdout.write('Geeks')

n = len(sys.argv) # give no of command line arguments
print(f"No of command line arguments:- {n}")
print(f"Name of the script:- {sys.argv[0]}")
print(f"All arguments:-")

for i in range(n):
    print(f"Argument:- {sys.argv[i]}")

sum=0
for i in range(1,n):
    sum+=int(sys.argv[i])
print(sum)

print(sys.path) # List all paths
print(sys.modules)
age = 17
if age < 18:
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")

