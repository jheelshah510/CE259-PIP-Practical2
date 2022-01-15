#20CS082 Jheel Shah
#Write a Python program to add member(s) in a set and clear a set

def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

set = {"a","b","c"}

items = [1,2,3,4]
set = addtoset(set,items)


print(set)