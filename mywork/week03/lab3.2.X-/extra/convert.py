# program that takes in a float amount of dollars and  returns that absolute amount in cent
amount=float(input('input a float amount: '))
absolute_amount=abs(amount)
value_in_cent=absolute_amount*100
print(f'the value in cents of {absolute_amount} is {value_in_cent}'. format(amount, absolute_amount, value_in_cent))