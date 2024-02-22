# program that inputs a bank account number and outputs the last 4 digits and replace the first 6 with Xs
accountNumber= input('input an account number: ')
masked_number= "X" * (len(accountNumber)-4) + accountNumber[-4:]
print(masked_number)
