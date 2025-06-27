
def greatest(a,b,c):
    if (a > b and a > c): 
        return f"{a} is greatest"
    elif (b > c):
        return f"{b} is greatest"
    else:
        return f"{c} is greatest"
    
print(greatest(4,5,6))