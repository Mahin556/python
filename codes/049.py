# 5
# 5+4
# 5+4+3
# 5+4+3+2
# 5+4+3+2+1

def sum(n):
    if (n==1):
        return 1
    if (n==0):
        return 0
    return n+sum(n-1)
print(sum(0))


