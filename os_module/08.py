import os
try:
    filename = 'GFG.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
  print('Problem reading: ' + filename)

# Python os module error class is the base class for I/O related errors. So we can catch IO errors using OSError in the except clause.

try:
    f = open('abc.txt', 'r')  # file is missing
except OSError:
    print('Error')