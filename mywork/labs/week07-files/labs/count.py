# a program that counts how many times it was run
# data stored outside the memory and accessible everytime the program it is run

FILENAME= "count.txt" #the filename is 

def writeNumber(number): #creating the new wtite function
    with open('count.txt', 'wt') as f: #open the file in a writing mode
        #this function takes two parametes number (the number to write to the file) and filename (the name of the file to overwrite)
        f.write(str(number))  #It attempts to open the file specified by filename in write mode ('w')
        # and writes the string representation of the number to the file using f.write(str(number))

def readNumber(): # creating the funtion and name it readNumber
    try: # try added later to check if the file exists 
        with open ('count.txt', 'r') as f: # opening the file(name) in a read mode and we name this command as f
         number=int(f.read()) # say to the funtion that the nymber to be read is an integer in f
         return number
    except IOError: # if the file doesn't exist it creates it with the value
        writeNumber(0)    
        return 0

number=readNumber() # recall to the funtion
# print the result
# This function attempts to open the file specified by the filename parameter in read mode ('r'). 
# It reads the content of the file using f.read() and converts it to an integer using the int() function. I
# It then returns this number.
# lastly with number we call the function and if the number is succesfully read it prints it


# b. Write a function that takes in a number and overwrites a file with that
# number (count.txt). test it and check that the file has been changed


#counting how many times the program was run
        
number=readNumber()

number+=1

print(f' we have run this program {number} times')

writeNumber(number)

