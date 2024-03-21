# a program that makes a list called ages that has the same random number value as salaries (range:21 to 65).
#make a scatter plot

import numpy as np
import matplotlib.pyplot as plt

minimum_salary = 2000
maximum_salary=8000
number_entries=10


salaries= np.random.randint(minimum_salary, maximum_salary, number_entries)
ages=np.random.randint(low=21, high=65, size= number_entries)
np.random.seed(1)
print(salaries)

plt.scatter(ages, salaries)
plt.title('ages and salaries')
plt.xlabel('ages')
plt.ylabel('salaries')
plt.savefig('prettier-agesalaries.png')
plt.show()

x=np.array(range(1,1001))
y=x*x

plt.scatter(x,y, color='r',label='y=x^2')
plt.title('y=x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('prettier-plot.png')
plt.show()


