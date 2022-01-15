#20CS082 Jheel Shah
#Write a Python program to add an item in a tuple.

def additem(t,item):
    l = list(t)
    l.append(item)
    t = tuple(l)
    return t

t = (1,2,3,4,5,6)
item = 9

t = additem(t,item)

print(t)