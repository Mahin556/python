# PADK

# parameters
# *args
# default parameters
# **kwargs

def func(name = 'unknown', age = 24):
    print(name)
    print(age)

func('harshit', 25)


def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('harshit', 1, 2, 3, a = 1, b = 2)

"""
harshit
(1, 2, 3)
unknown
{'a': 1, 'b': 2}

"""