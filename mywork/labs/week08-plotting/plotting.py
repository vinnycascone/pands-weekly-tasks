# a program that plots the function y=x^2

import numpy as np
import matplotlib.pyplot as plt

x=np.array(range(1,1001))
y=x*x

plt.plot(x,y)
plt.savefig('plot')
plt.show()

