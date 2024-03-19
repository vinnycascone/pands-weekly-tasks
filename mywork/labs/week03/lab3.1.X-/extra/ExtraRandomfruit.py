# This program prints out a random fruit
import random
def get_random_fruit():
fruits = ['apple', 'orange', 'banana', 'pear']
return random.choice(fruits)
if __name__== "__main__":
print("a random fruit is: " get_random_fruit())