print (1,2,3, end= "\t", sep="")
print ('hi')

# un named arguments
def fun1(*args):
    print(type(args))
    for val in (args):
        print(val)

fun1("a", "b", "c")

def fun2(**kwargs):#keyword arg
    print(type(kwargs))
    print(kwargs)
    #for val in (kwargs):
        #print(val)
    
#fun2(name="joe", age=21, gender="M")

#sample code
def ave(*values):
    number_of_values=len(values)
    sum=0
    for value in values:
        sum += value
    average= sum / number_of_values
    return average

print(ave(1,2,3,4,5,6))
