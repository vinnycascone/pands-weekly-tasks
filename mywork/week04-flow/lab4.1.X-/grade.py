# a program that reads in a student’s percentage mark and prints out corresponding the grade

# percentage valid:
# Under 40% => Fail
# Between 40% and 49% => Pass
# Between 50% and 59% => Merit 2
# Between 60% and 69% => Merit 1
# Over 70% => Distinction

percentage= float(input('input the percentage value: '))
print(f'The percentage is {percentage}')

if percentage < 40: 
 print('The grade is Fail')

elif percentage < 50:
    print('The grade is Pass')
elif percentage < 60:
    print('The grade is Merit 2')
elif percentage < 70:
   print(' The grade is Merit 1')

else:
    print(' The grade is distinction')

 
