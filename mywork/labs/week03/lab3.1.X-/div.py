# program that reads in two numbers and
# outputs the integer answer and remainder
x = int (input ("Enter the first number: "))
y = int (input( "Enter the second number: "))
answer = int (x // y)
remainder= x % y
print (f"{x} divided by {y} is {answer} with the remainder of {remainder}".format(x,y,answer,remainder))
