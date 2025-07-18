# ===============================
# Python sys Module Overview
# ===============================

# The `sys` module provides access to Python interpreter variables and functions.
# It's useful for command-line arguments, input/output redirection, version info,
# program exit, recursion settings, module handling, etc.

import sys

# -------------------------------
# 1. Python Version
# -------------------------------
print("Python version:")
print(sys.version)

# -------------------------------
# 2. Command-Line Arguments
# -------------------------------

# sys.argv holds all the command-line arguments passed to the script.
print("\nCommand-line arguments:")
print("Script name:", sys.argv[0])
print("Arguments passed:", sys.argv[1:])

# Example: Sum all command-line arguments passed as numbers
total = 0
for i in range(1, len(sys.argv)):
    total += int(sys.argv[i])
print("Sum of numeric arguments:", total)

# -------------------------------
# 3. Input from stdin
# -------------------------------
# Read from standard input (useful for redirection)
# Type 'q' to stop input
print("\nReading from stdin. Type 'q' to quit:")
# Uncomment below to test
# for line in sys.stdin:
#     if line.strip() == 'q':
#         break
#     print("Input:", line.strip())

# -------------------------------
# 4. Output to stdout
# -------------------------------
sys.stdout.write("\nThis was written to stdout\n")

# -------------------------------
# 5. Output to stderr
# -------------------------------
print("This is an error message", file=sys.stderr)

# -------------------------------
# 6. Exiting the Program
# -------------------------------
age = 17
if age < 18:
    sys.exit("Exit: Age must be 18+ to proceed.")
print("You are allowed to continue.")  # Won’t run if exited above

# -------------------------------
# 7. sys.path - Module Search Path
# -------------------------------
print("\nPython module search paths:")
for p in sys.path:
    print(p)

# You can modify it at runtime:
# sys.path.append("/my/custom/path")

# -------------------------------
# 8. sys.modules - Loaded Modules
# -------------------------------
print("\nCurrently loaded modules:")
print(list(sys.modules.keys())[:10])  # Print first 10 module names

# -------------------------------
# 9. sys.getrefcount - Reference Count
# -------------------------------
a = "Geeks"
print(f"\nReference count for object 'a': {sys.getrefcount(a)}")

# -------------------------------
# 10. Other Useful Functions
# -------------------------------

# Get and set recursion limit
print("\nCurrent recursion limit:", sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

# sys.maxsize
print("Maximum size of a Python int:", sys.maxsize)

# sys.getdefaultencoding
print("Default encoding:", sys.getdefaultencoding())

# sys.setswitchinterval
print("Setting thread switch interval to 0.01s")
sys.setswitchinterval(0.01)
