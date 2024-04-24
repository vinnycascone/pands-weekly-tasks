README.md

# Weekly Assignments executed by Vincenzo Cascone

In this readme file you'll find the explanation of all the coding that I have executed for the weekly Tasks.

## Week02 Assignment:

Here's a breakdown of what I have done:

- Created two variables
  - `amount1`: Prompted the user to input the first amount in cents and stored it in the variable amount1. The int() function is used to convert the input (which is initially a string) into an integer.
  - `amount2`: Same command here

- Calculated the totalAmount
  - `totalAmount`: Calculated the total amount by adding amount1 and amount2 together.

- Divided the number to get the whole number and the remaining cents
  - `euro`: Calculated the euro part of the total amount by integer division (//) of the total amount by 100. This gives the whole euro part of the amount.
  - `cent`: Calculated the cent part of the total amount by taking the remainder (%) when the total amount is divided by 100. This gives the remaining cents after removing the euro part.

- Printed the outcome with the right formatting
  - `print(f" the sum of these is: €{euro}.{cent}")`: Printed out the sum of amount1 and amount2 in euro format, where {euro} represents the euro part and {cent} represents the cent part of the total amount. The f-string formatting is used here to embed variables (euro and cent) within the string.

references: 
- Numeric Types - int, float, complex: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex



## Week03 assignments:

### Accounts.py:

In this code, I prompted the user to input a 10-digit account number and then masked the first six digits, replacing them with "xxxxxx". Here's a breakdown of how I worked:

- Created the variable account number by prompting the user to input.
  - `accountNumber`: Prompted the user to input a 10-digit account number and stored it as a string in the variable accountNumber.

- Created a variable called `masked_number` to replace the last digits with a concatenation of X.
  - `masked_number`: Created a new string masked_number by concatenating "xxxxxx" with a slice of accountNumber starting from index 6 up to index 9 (10 is exclusive). This effectively masks the first six digits of the account number, leaving only the last four digits visible.

Given the print command
  - `print(masked_number)`: Printed the masked_number, which is the masked version of the account number with "xxxxxx" replacing the first six digits.


### unlimited accounts.py :

In this code, I took an account number as input and then masked all but the last four digits with 'X' characters. Here's how I worked:

- Created the variable account number by prompting the user to input.
  - `accountNumber`: Prompted the user to input an account number and stored it as a string in the variable accountNumber.

- Created a variable called `masked_number` to replace some digits with a concatenation of X.
  - `masked_number`: Constructed the masked version of the account number.
    - `"X" * (len(accountNumber)-4)`: Generated a string of 'X' characters whose length is equal to the length of accountNumber minus 4. This effectively masked all but the last four digits.
    - `accountNumber[-4:]`: Concatenated the last four digits of accountNumber to the masked string generated in the previous step. This ensured that the last four digits remain visible.

Given the print command
  - Printed the masked_number, which is the masked version of the account number with 'X' characters replacing all but the last four digits.


references:
- String method: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str





## Week04:
### Collatz.py:

In this code, I defined a Python function collatz(n) that generates the Collatz sequence for a given positive integer n. Here's how I worked:

- I have defined the function ‘def collatz(n)’  that takes one parameter n, representing the starting number for the Collatz sequence.

- Created a while loop
  - `while n > 1::` started a while loop that continues until n becomes 1. The Collatz sequence terminates when it reaches the number 1.

Given print command
  - `print(n, end=' ')`: Printed the current value of n without a newline character (using end=' ') to display the sequence in a single line.

- Added the condition if to verify if the number is odd
  - `if (n % 2)::` Checked if n is odd by checking the remainder when n is divided by 2 (n % 2). If the remainder is non-zero, it means n is odd.
  - If n is odd, it updates n to 3*n + 1, according to the Collatz conjecture.

- Created the condition of the even number with else
  - `else::` Executed if n is even (when (n % 2) evaluates to 0).
  - Stated that the number is even i have updated n to n//2, effectively halving the value.

Given the print command after the while loop
  - `print(1, end=' ')`: After the while loop terminates (when n becomes 1), printed the final value of 1 to complete the sequence, also without a newline character.

- Giving the prompt command and converting it to an integer outside of the function for modularity and reusability so It can be reused with different initial values of n without needing to modify the function itself.
  - `n = int(input('Enter a positive number: '))`: Prompted the user to input a positive number and converted it to an integer, storing it in the variable n.

- Given the print command to print the initial message
  - `print('Sequence: ', end='')`: Printed the initial message for the Collatz sequence.

- Last, calling the function
  - `collatz(n)`: Called the collatz function with the user-input integer n to generate and print the Collatz sequence starting from n.


reference: 
- Functions: https://www.w3schools.com/python/python_functions.asp
- While statement: https://docs.python.org/3/reference/compound_stmts.html#while





## Week05:
### weekday.py

In this code, I utilized the datetime module in Python to determine whether the current day is a weekday or the weekend. Here's a breakdown:

- Imported the datetime module
  - `from datetime import datetime`: Imported the datetime class from the datetime module for methods on how to work with dates and times in Python.

- Retrieved the current day
  - `current_day = datetime.now().weekday()`: Retrieved the current day of the week as an integer using the weekday() method of the datetime object returned by datetime.now(). The days of the week are represented as integers from 0 (Monday) to 6 (Sunday).

- Created a conditional statement:
  - `if current_day < 5::` Checked if the current day (represented by current_day) is less than 5, which corresponds to Monday to Friday (0 to 4). If true, it means it's a weekday.

Given print command
  - `print("Yes, unfortunately today is a weekday.")`: Printed a message indicating that it's a weekday.

  - `else::` If the current day is not less than 5, it means it's Saturday or Sunday (5 or 6).
  - Given the second print command
  - `print("It is the weekend, yay!")`: Printed a message indicating that it's the weekend.


reference: https://www.w3schools.com/python/python_datetime.asp






## Week06:
### sqrt.py:

With this code, I have defined a function sqrt(a, tolerance=1e-7) to compute the square root of a positive number a with a specified tolerance. Here's what I did:

- Function Definition:
  - `def sqrt(a, tolerance=1e-7)`: Defined a function named sqrt that takes two parameters: a, the number whose square root is to be computed, and tolerance (with a default value of 1e-7), which determines the accuracy of the approximation.

- Input Validation:
  - Check if the input is negative. If so, I printed a message indicating that the square root of a negative number cannot be computed and returns None.

- Initial Approximation:
  - Sets an initial approximation x for the square root. If a is greater than or equal to 1, it initializes x to a/2; otherwise, it sets x to 1.

- Iterative Calculation:
  - Used a loop to iteratively refine the approximation of the square root.
  - Updates the approximation x using the formula: next_x = 0.5 * (x + a/x), which is based on Newton's method for finding roots.
  - The loop continues until the absolute difference between x and next_x is less than the specified tolerance.

- Input and Output:
  - Prompted the user to input a positive number.
  - Called the sqrt function with the input number to compute the approximate square root.
  - Printed the result if it's not None, indicating that the square root computation was successful.


references:
- Newton Raphson method for finding the roots
Scientific Notation 1e-7 used to define the approximation of the root number by one milionth





## Week07:
### es.py

This code reads a text file specified as a command-line argument and counts the occurrences of the letter 'e' in the file. Here's a summary of what I did:

- Imported OS to to use operation system functions such as to see if file exists or not and imported sys to receive arguments from the system

- Function Definition:

  - `count_es(filename)`: Defined a function that takes a filename as input.
    - Opened the file specified by filename in read mode ('r'), read its contents and returned the conversion to lowercase, counted the occurrences of the letter 'e' using the count() method.

- Error Handling:

  - Handled two types of exceptions:
    - FileNotFoundError: Raised when the specified file is not found.
    - Exception: Handled other exceptions that might occur during file processing.

- Processing:

  - Checked if the number of command-line arguments is not equal to 2 (the script name and the filename). If not, prints a usage message and exits.
  - Assigned the provided filename from the command-line argument to the variable filename.
  - Checked if the provided filename is a valid text file (ends with '.txt') and exists using os.path.isfile() and .endswith(). If not, to print an error message and exit.

- Counted 'e's in the File:

  - Called the count_es function with the provided filename and stored the result in the variable e_count.
  - Printed the count of 'e' occurrences.

references:
- Reading and Writing Files in Python (Guide): https://realpython.com/read-write-files-python/
- Exception Handling in Python: https://docs.python.org/3/tutorial/errors.html
- Python File System Access (os module): https://www.geeksforgeeks.org/os-module-python-examples/
- Python exit commands: https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/



## Week08:
### plottask.py

In this code, I utilized Matplotlib to generate a histogram of 1000 random values drawn from a normal distribution, along with the plot of the function h(x)=x ^3 in the range [0,10]

Here's a breakdown of what I did:

- Imported the libraries:
  - `import matplotlib.pyplot as plt`: Imported the Matplotlib library and aliases it as plt.
  - `imported numpy as np`: Imported the NumPy library and aliases it as np.

- Generated Random Values:
  - `mean = 5`: Sets the mean (μ) of the normal distribution to 5.
  - `std_dev = 2`: Sets the standard deviation (σ) of the normal distribution to 2.
  - `values = np.random.normal(mean, std_dev, 1000)`: Generated 1000 random values from a normal distribution with the specified mean and standard deviation using NumPy's random.normal() function.

- Plotted Histogram:
  - `plt.hist(values, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution')`: Plotted a histogram of the generated values with 30 bins, normalized to form a probability density, and with a transparency of 0.5. The histogram is colored blue and labeled as "Normal Distribution".

- Plotted the Function h(x)=x^3
  - `x = np.linspace(0, 10, 100)`: Generated 100 equally spaced values between 0 and 10 using NumPy's linspace() function.
  - `y = x ** 3`: Calculated the corresponding y values using the function h(x)=x^3
  - `plt.plot(x, y, color='red', label='$h(x) = x^3$')`: Plotted the function h(x)=x^3 with red color and labeled it accordingly using LaTeX syntax.

- Added Legend and Labels:
  - `plt.legend()`: Added a legend to the plot.
  - `plt.xlabel('Value')`: Added a label to the x-axis.
  - `plt.ylabel('Frequency/Density')`: Added a label to the y-axis.
  - `plt.title('Histogram of Normal Distribution and Function $h(x) = x^3$')`: Added a title to the plot using LaTeX syntax for rendering mathematical expressions.

- Displayed the Plot:
  - `plt.grid(True)`: Added gridlines to the plot.
  - `plt.show()`: Displayed the plot.

Overall, with this code I created a visual representation of a histogram for random values drawn from a normal distribution and plotted the function h(x)=x^3 on the same plot.


references:
- Matplotlib: https://matplotlib.org/stable/contents.html
- NumPy:https://numpy.org/doc/stable/ 