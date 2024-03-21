# a program that plots a histogram from salaries.py

import numpy as np
import matplotlib.pyplot as plt

minimum_salary = 2000
maximum_salary=8000
number_salaries=10


salaries= np.random.randint(minimum_salary, maximum_salary, number_salaries)
np.random.seed(1)
print(salaries)

plt.hist(salaries)
plt.savefig('salaries')
plt.show()