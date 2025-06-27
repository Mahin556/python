
def demo(name,reverse_str=False):
    if reverse_str==True:
        name=name[-1::-1]
    return name.capitalize()

print(demo("mahin"))
print(demo("mahin",reverse_str=True))


def demo2(names,**kwargs):
    if kwargs.get("reverse_str") == True:
        return [name[-1::-1].capitalize() for name in names]
    else:
        return [name.capitalize() for name in names]

l=["mahin","raza"]
print(demo2(l))
print(demo2(l,reverse_str=True))