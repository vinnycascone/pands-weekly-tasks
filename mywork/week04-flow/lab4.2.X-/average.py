# a program that keeps reading numbers until user enters a zero ( append into a list)
# print out each number and calculate average

numbers = []

number = int(input ('input a number (0 to quit): '))

while number != 0 :
    numbers.append(number)
    number = int(input('input a new number (0 to quit): '))


for value in numbers:
    print (value)


average = float(sum(numbers)) / len(numbers)
print(f'the average is {average}')
