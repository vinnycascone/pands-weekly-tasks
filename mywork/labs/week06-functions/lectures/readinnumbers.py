# read in numbers and multiply them



# making a loop for someone entering always a string
#num1= False

#while (num1 == False):
#catch exceptions
    #try:
     # num1 =int(input("enter a number"))
    #except ValueError:
     # print("no strings, a number please")


#num2 = False
#while (num2 == False):
#catch exceptions
 #    try:
 #      num2 =int(input("enter another number"))
 #   except ValueError:
 #     print("no strings, a number please")

def readNum (message = "enter a number"):
   num=False
   while (num == False):
#catch exceptions
         try:
             num =int(input(message ))
         except ValueError:
             print("no strings, a number please ")
         return num

num1=readNum()
num2=readNum()

answer = num1 * num2
print(f"answer is {answer}")