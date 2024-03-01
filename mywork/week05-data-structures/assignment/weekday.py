# importing datetime from datetime library
from datetime import datetime

# Get the current day of the week (0 is Monday, 6 is Sunday)
current_day = datetime.now().weekday()


if current_day < 5:  # Monday to Friday
    print("Yes, unfortunately today is a weekday.")
else: 
    print("It is the weekend, yay!")