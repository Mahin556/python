#!/bin/python3
import sys

arg1 = sys.argv[1]

if arg1 == "--help":
    print("To print the pricing of instance types")
elif arg1 == "t2.micro":
    print("$2 for a day")
else:
    print("Invalid argument")