#20CS082 Jheel Shah
#Write a Python program to convert a tuple to a string.

def toString(t):
    string = ""
    for i in t:
        string = string + str(i)
    return string

t = ('a','b','c')

string = toString(t)

print(string)