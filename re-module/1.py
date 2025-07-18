# http://w3schools.com/python/python_regex.asp
# https://www.geeksforgeeks.org/python/regular-expression-python-examples/
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)