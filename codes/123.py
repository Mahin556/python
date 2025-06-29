#MAP FUNCTION

number=[1,2,3,4]

def square(a):
    return a**2

square_=list(map(square,number))
print(square_)

square1=list(map(lambda a:a**2,number))
print(square1)

names=["mahin","raza","john"]
lens=list(map(len,names))
print(lens)