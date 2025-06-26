import sys
import pyjokes


print("Printing version.....")
print(sys.version)
print("Printing joke.....")
joke=pyjokes.get_joke()
print(joke)
print("\nHello, World!")