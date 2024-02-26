# system generates the random number

import random
number_to_guess= random.randint (0,100)
print(f'the random number is {number_to_guess}')
number=int(input('please input the number to guess:'))

while number != number_to_guess:
    if number < number_to_guess: 
     print('Wrong, number is too low')
    if number > number_to_guess:
       print('Wrong, the number is too high')
    number=int(input('please input a new number: '))

print ('correct')