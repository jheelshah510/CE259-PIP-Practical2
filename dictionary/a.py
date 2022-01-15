#20CS082 Jheel Shah
#  a. Write a Python script to check whether a given key already exists in a dictionary.


#sample dictionary
dict = {'A': 1, 'B':2, 'C':3}

#key to find if it exists
key = 'A'
#if key is present in dictionary
if key in dict:
        print("Present")
        
else:
        print("Not present")

#key to find if exists  
key = 'D'
#if key is present in dictionay
if key in dict:
    print("Exists")
#else    
else:
    print("Not present")