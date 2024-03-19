# import json

# FILENAME= 'json.txt'
# sample = dict(name='Vincenzo', age=32, grades= [100,95,90] ) #way to create dictionary
# # print(sample)

# def writeDictionary(obj):
#     with open(FILENAME, 'wt') as f:
#         json.dump(obj,f)
        
# writeDictionary(sample)

# we have taken a dictionary and stored as json into a file
import json 
FILENAME="test.json" 
sample= dict(name='fred', age=31, grades=[1,34,55]) 
def writeDict(obj): 
    with open(FILENAME, 'wt') as f: 
        json.dump(obj,f) #test the function writeDict(sample)

# writeDict(sample)

#we are opening a file and retrieving json as a dictionary
def readDict():
    with open(FILENAME) as f:
        return json.load(f)
    
a=readDict()
print(a)


