# program that inputs a 10 digit bank account number and outputs the last 4 digits and replace the first 6 with Xs
accountNumber= input('input a 10 digit account number: ')
masked_number= "xxxxxx" + accountNumber[6:10]
print(masked_number)
