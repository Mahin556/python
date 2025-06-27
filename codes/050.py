def pattert(n):
    if n==0:
        return
    print("*"*n)
    pattert(n-1)

pattert(5)