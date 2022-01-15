#20CS082 Jheel Shah 
#  b. Write a Python script to merge two Python dictionaries.



#function to mrege two dictionaries
def mergedict(dict1,dict2):
    #for every key in dict2 add that key and value to dict1
    for key in dict2.keys():
        dict1[key] = dict2[key]
    #return dict1
    return dict1

# sample dictionaries
dict1 ={"a":1,"b":2,"c":3}

dict2 ={"d":4,"e":5,"f":6}
#mrege dict1 and dict2 to form dict3
dict3 = mergedict(dict1,dict2)
#print dict3
print(dict3)