
def finder(num,*args):
    if not args:
        print("You doesn't pass any args please pass arguments")
        exit
    else:
        return [x**num for x in args]
    
print(finder(2,1,2,3,4,5,6,7,8))