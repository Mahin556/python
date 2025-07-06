def func_1(*args):
    avg=[]
    for i in zip(*args):
        avg.append(sum(i)/len(i))
    return avg

def func_2(*args):
    return [ (sum(i)/len(i)) for i in zip(*args) ] 

func_3= lambda *args : [ (sum(i)/len(i)) for i in zip(*args) ]

print(func_1([1,2,3],[4,5,6],[7,8,9]))
print(func_2([1,2,3],[4,5,6],[7,8,9]))
print(func_3([1,2,3],[4,5,6],[7,8,9]))

