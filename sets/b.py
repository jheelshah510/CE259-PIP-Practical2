#20CS082 Jheel Shah
#b. Write a Python program to remove an item from a set if it is present in the set.

def removeitem(set,item):
    set.discard(item)
    return set



set = {1,2,3,4,5,6,7}

set = removeitem(set,6)

print(set)
set = removeitem(set,100)

print(set)