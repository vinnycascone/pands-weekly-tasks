# a program that asks a user to input a positive integer and outputs
#if it is even
# divide by two
# if it is odd
# multiply by three
# add one

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    print(1, end=' ')
 
 
n = int(input('Enter a positive number: '))
print('Sequence: ', end='')
collatz(n)