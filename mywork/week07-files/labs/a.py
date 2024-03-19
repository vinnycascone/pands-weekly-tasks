with open("test-a.txt") as f:
 data = f.read()
 print (data)

# the program will find an error as the file doesn't exist
# so we need to create the file
# also the print command is inside the with function so it won't print anything as with will automatically close the file
# inside the brackets is not indicated the command of reading 