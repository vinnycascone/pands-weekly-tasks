# program that reads in a string and strips any leading spaces
# also convert the string to lower case
# output the length of the input and output strings
inputString= input('enter a string:')
newString= inputString.strip().lower()

lengthInput=len(inputString)
lengthOutput=len(newString)
print(f'the string adjusted is {newString} and its length passed from {lengthInput} to {lengthOutput}')
