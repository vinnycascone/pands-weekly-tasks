# a program that makes a list

import numpy as np

minimum_salary = 2000
maximum_salary=8000
number_salaries=10


salaries= np.random.randint(minimum_salary, maximum_salary, number_salaries)
np.random.seed(1)
print(salaries)

new_salaries=np.array(salaries + 5000)
print(new_salaries)

increased_salaries=np.array(new_salaries*1.05)
print(increased_salaries)

