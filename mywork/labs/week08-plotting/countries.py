# a program that picks five countries (pick from five)
# make some countries appear more than others
# make a piechart

import numpy as np
import matplotlib.pyplot as plt

countries=('Italy', 'France', 'Ireland','Spain', 'England')
countries_pick= np.random.choice(
    countries, 
    p=[0.1, 0.3, 0.2, 0.12, 0.28], 
    size=(100))
print(countries_pick)

#finding the number of occurrency per country

unique, counts= np.unique(countries_pick, return_counts=True)

plt.pie(counts, labels=unique)

plt.show()