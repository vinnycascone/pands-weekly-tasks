# a program that puts 10 random numbers into a queue list
# output all the values 
# take the numbers one at the time, print it and the current numbers still in the queue
# command pop(0) takes the first element out of a list

import random

queue = [] 
range_to = 100

for n in range (0, 10): 
    queue.append(random.randint(0, range_to))
print(f'queue is: {queue}')

while len(queue) != 0:
    current_number= queue.pop(0)
    print(f'current number is {current_number} and the queue is {queue}')

print('the queue is now empty')
