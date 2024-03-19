with open("test-b.txt", "w") as f:
 data = f.write("test b\n") # returns the number of chars written
 print (data)

# The first with block opens the file "test-b.txt" in write mode ("w"). 
# It writes the string "test b\n" into the file and returns the number of characters written, which is 7 
# This value is stored in the variable data and printed, so you will see 7 printed.
 
with open("test-b.txt", "w") as f2: # open file again
 data = f2.write("another line\n")
 print (data)

# The second with block also opens the same file "test-b.txt" in write mode ("w").
# It writes the string "another line\n" into the file, overwriting any existing content.
# Again, it returns the number of characters written, which is 13 (including the newline character). This value is stored in the variable data and printed, so you will see 13 printed.
 
# As a result, the file "test-b.txt" will contain only the text "another line\n" because the second write operation overwrites the content written in the first operation.
