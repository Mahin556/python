#The platform module is a built-in Python library that provides a portable way to access detailed information about the underlying system and hardware where your Python program runs.

import platform
print(platform.processor()) #CPU info

print(platform.architecture()) #Python architecture (32/64-bit)	

print(platform.machine()) #Hardware architecture

print(platform.node()) #Hostname

print(platform.platform())	#Full platform string

print(platform.system()) #OS name

print(platform.uname()) #Full system summary (tuple)

print(platform.python_version()) #Python version

print(platform.python_build()) #Build metadata

print(platform.python_compiler()) #Compiler info

print(platform.python_implementation()) #Implementation used

print(platform.python_branch()) #Branch of Python source

