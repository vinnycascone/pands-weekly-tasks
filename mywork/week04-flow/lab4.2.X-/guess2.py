# the program tells if the guess is too high or too low

number_to_guess=30
number=int(input('please input the number to guess:'))

while number != number_to_guess:
    if number < number_to_guess: 
     print('Wrong, number is too low')
    if number > number_to_guess:
       print('Wrong, the number is too high')
    number=int(input('please input a new number: '))

print ('correct')