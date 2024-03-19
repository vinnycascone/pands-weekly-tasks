# I used the Newton Raphson method 
# # the method starts from an initial value and it's used to determine when to stop iterating
# the method helps defining how precise the approximation shuold be by considering the value 1e-7
# the tolerance is there to tell how precise the value should be
# creating the function to calculate the approximation of the square root without using sqrt function
def sqrt(a, tolerance=1e-7):
    if a<0:
        print ("Cannot compute the square root of a negative number")
        return None 
    if a >=1: 
        x=a/2
    else:
        x=1 
    while True:
        next_x= 0.5 * (x+a/x)
        if abs(x-next_x) < tolerance:
          return x
        x = next_x


number=float(input('enter a positive nnumber to find a square root of: '))
approximate_sqrt = sqrt(number)


if approximate_sqrt is not None:
    print(f"The square root of {number} is approximately {approximate_sqrt}")
