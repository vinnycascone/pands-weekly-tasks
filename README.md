README.md

Weekly assignments executed by Vincenzo Cascone:

Week02 Assignment:
Here's a breakdown of what I have done:

Created two variables
amount1 = Prompted the user to input the first amount in cents and stored it in the variable amount1. The int() function is used to convert the input (which is initially a string) into an integer.
amount2 = same command here

Calculated the totalAmount
totalAmount = Calculated the total amount by adding amount1 and amount2 together.

Divided the number to get the whole number and the remaining cents
euro = Calculated the euro part of the total amount by integer division (//) of the total amount by 100. This gives the whole euro part of the amount.
cent = Calculated the cent part of the total amount by taking the remainder (%) when the total amount is divided by 100. This gives the remaining cents after removing the euro part.

Printed the outcome with the right formatting
print(f" the sum of these is: €{euro}.{cent}"): Printed out the sum of amount1 and amount2 in euro format, where {euro} represents the euro part and {cent} represents the cent part of the total amount. The f-string formatting is used here to embed variables (euro and cent) within the string.


Week03 assignments:

Accounts.py:

This code prompts the user to input a 10-digit account number and then masks the first six digits, replacing them with "xxxxxx". Here's a breakdown of how I worked:

Created the variable account number by prompting the user to input.
accountNumber = Prompted the user to input a 10-digit account number and stored it as a string in the variable accountNumber.

Created a variable called masked_number to replace the last digits with a concatenation of X.
masked_number = Created a new string masked_number by concatenating "xxxxxx" with a slice of accountNumber starting from index 6 up to index 9 (10 is exclusive). This effectively masks the first six digits of the account number, leaving only the last four digits visible.

Given the print command
print(masked_number): Printed the masked_number, which is the masked version of the account number with "xxxxxx" replacing the first six digits. 



This code takes an account number as input and then masks all but the last four digits with 'X' characters. Here's how I worked:

Created the variable account number by prompting the user to input.
accountNumber = Prompted the user to input an account number and stored it as a string in the variable accountNumber.

Created a variable called masked_number to replace some digits with a concatenation of X.
masked_number = Constructed the masked version of the account number.
"X" * (len(accountNumber)-4)= Generated a string of 'X' characters whose length is equal to the length of accountNumber minus 4. This effectively masked all but the last four digits.
+ accountNumber[-4:]= Concatenated the last four digits of accountNumber to the masked string generated in the previous step. This ensured that the last four digits remain visible.

Given the print command
Printed the masked_number, which is the masked version of the account number with 'X' characters replacing all but the last four digits. 




Week04:
Collatz.py:

This code defines a Python function collatz(n) that generates the Collatz sequence for a given positive integer n. Here's how I worked:

I have defined the function ‘def collatz(n)’  that takes one parameter n, representing the starting number for the Collatz sequence.

Created a while loop
while n > 1:: started a while loop that continues until n becomes 1. The Collatz sequence terminates when it reaches the number 1.

Given print command
print(n, end=' '): Printed the current value of n without a newline character (using end=' ') to display the sequence in a single line.

Added the condition if to verify if the number is odd
if (n % 2)::Checked if n is odd by checking the remainder when n is divided by 2 (n % 2). If the remainder is non-zero, it means n is odd.
If n is odd, it updates n to 3*n + 1, according to the Collatz conjecture.

Created the condition of the even number with else
else::Executed if n is even (when (n % 2) evaluates to 0).

Stated that the number is even i have updated n to n//2, effectively halving the value.

Given the print command after the while loop
print(1, end=' '): After the while loop terminates (when n becomes 1), printed the final value of 1 to complete the sequence, also without a newline character.

Giving the prompt command and converting it to an integer outside of the function for modularity and reusability so It can be reused with different initial values of n without needing to modify the function itself.
n = int(input('Enter a positive number: ')): Prompted the user to input a positive number and converted it to an integer, storing it in the variable n.

Given the print command to print the initial message
print('Sequence: ', end=''): Printed the initial message for the Collatz sequence.

Last, calling the function
collatz(n): Called the collatz function with the user-input integer n to generate and print the Collatz sequence starting from n.

reference: https://www.w3schools.com/python/python_functions.asp




Week05:
weekday.py

This code utilizes the datetime module in Python to determine whether the current day is a weekday or the weekend. Here's a breakdown:

Importing the datetime module
from datetime import datetime: Imported the datetime class from the datetime module for methods on how to work with dates and times in Python.

Retrieved the current day
current_day = datetime.now().weekday(): Retrieved the current day of the week as an integer using the weekday() method of the datetime object returned by datetime.now(). The days of the week are represented as integers from 0 (Monday) to 6 (Sunday).

Created a conditional statement:
if current_day < 5:: Checked if the current day (represented by current_day) is less than 5, which corresponds to Monday to Friday (0 to 4). If true, it means it's a weekday.

Given print command
print("Yes, unfortunately today is a weekday."): Printed a message indicating that it's a weekday.
else:: If the current day is not less than 5, it means it's Saturday or Sunday (5 or 6).
Given the second print command
print("It is the weekend, yay!"): Printed a message indicating that it's the weekend.

reference: https://www.w3schools.com/python/python_datetime.asp

