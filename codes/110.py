import datetime

x = datetime.datetime.now()
print(x)

"""2025-06-28 11:25:21.876465"""

# Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))



# Creating Date Objects

y=datetime.datetime(2020,10,7)
print(y)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).


# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


# https://www.w3schools.com/python/python_datetime.asp