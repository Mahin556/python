
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

while True: 
    try:
        age=int(input('enter your age: ')) # seven # 7 
    except ValueError:
        print("Enter a number instead of string and try again")
    except:
        print('Unexpected error')
    else:
        break  #enhance readablity
    finally:
        print("Run always")


if age < 18:
    print('You can\'t play this game.')
else:
    print('you can play this game.')