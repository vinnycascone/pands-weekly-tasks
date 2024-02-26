# a program that prompts the user to guess a number until the user gets the right on
# please guess the number:2
# Wrong
# Please guess again:5
# Wrong
# Please guess again:30
# well done the number was 30

number_to_guess=30
number=int(input('please input the number to guess:'))

while number != number_to_guess:
    print('Wrong')
    number=int(input('please input a new number: '))

print ('correct')
