#20cs082 Jheel shah
#Write a Python program to find the length of a tuple.
def tulength(tuple):
    length = 0
    for _ in tuple:
        length +=1
    return length


tuple = ("apple", 1, "jheel")


print(len(tuple))