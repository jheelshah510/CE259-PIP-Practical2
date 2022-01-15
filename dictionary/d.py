#20CS082 Jheel Shah
# d.Write a Python script to add a key to a dictionary.

#Sample Dictionary : {0: 10, 1: 20}

#Expected Result : {0: 10, 1: 20, 2: 30}

def addkey(dict,keyname,keyvalue):
    dict[keyname] = keyvalue
    return dict

dict = {0: 10, 1: 20}
keyname = 2
keyvalue = 30

dict = addkey(dict,keyname,keyvalue)

print(dict)