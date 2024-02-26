# percentages are rounded ie 69.5 rounded to 70

percentage= float(input('input the percentage value: '))
rounded_percentage= round(percentage)
print(f'The percentage is {rounded_percentage}')

if rounded_percentage < 40: 
 print('The grade is Fail')

elif rounded_percentage < 50:
    print('The grade is Pass')
elif rounded_percentage < 60:
    print('The grade is Merit 2')
elif rounded_percentage < 70:
   print(' The grade is Merit 1')

else:
    print(' The grade is distinction')

while rounded_percentage != '-1': 
    rounded_percentage = (input(' input the percentage value: (enter -1 to exit)'))
print('all done')