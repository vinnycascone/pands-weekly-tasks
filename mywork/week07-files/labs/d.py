with open("test-d.txt", "w") as f:
    data = f.write("test d\n")  # Returns the number of chars written
    print(data)

with open("test-d.txt", "a") as f2:  # Open file again, this time in append mode ("a")
    data = f2.write("another line\n")
    print(data)

# same issue, the file doesn't exist so with is sending a write command which is printing the length of the string 7
# the second with is appending so will append the string as the file doesn't exist, again result of 13
    