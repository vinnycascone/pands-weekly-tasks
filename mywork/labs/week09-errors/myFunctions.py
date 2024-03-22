# a function called fibonacci that takes a number and returns a list containing a fibonacci
import logging
#logging.basicConfig(level=logging.DEBUG)

def fibonacci(n):
    if n<0:
        raise ValueError ("input an integer")
    a=0
    b=1
    fibonacci_sequence=[0]
    for i in range(1,n):
        fibonacci_sequence.append(b)
        a,b=b,a+b
    logging.debug("%d: %s", n,fibonacci_sequence)
    return fibonacci_sequence


#if __name__== "__main__":
   #test_cases=[0,1,7,11]
#function that contains the testing code

return7=[0,1,1,2,3,5,8]
return11=[0,1,1,2,3,5,8,13,21,34,55]
#assert fibonacci(7)==return7, 'the sequence is correct'
#assert fibonacci(11)==return11, 'the sequence is correct'
#assert fibonacci(0)==[], "sequence doesn't exist"
#assert fibonacci(1)==[1], "incorrect return"

#for n in test_cases: #creating the expected return options based on the input
#    result=fibonacci(n)
#    if n==0:
#        expected=[]
#    elif n==1:
#        expected = [1]
#    elif n==7:
#        expected =[return7]
#    elif n==11:
#        expected=[return11]

#status= 'OK' if result == expected else 'Failed'
#print(f"fibonacci({n})= {result}, expected:{expected}. Status: {status}")

try: #if the input is less than 0
    fibonacci(-1)
except ValueError: # we throw in the value error
    print('input validation passed')
else: #if exception not thrown we throw the assertion that the sequence is still missing
    assert False, 'Fibonacci still missing'


