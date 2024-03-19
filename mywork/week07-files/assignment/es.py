import os
import sys

# Import OS to use operation system functions such as to see if file exists or not
# importing sys to receive arguments from the system such as the string that is passed after python weekly.py string..txt
# Assumption 1 we making is that we will read all the e from the program even if its lower case.


def count_es(filename):
    try: 
        with open(filename, 'r') as file:
            contents = file.read()
            return contents.lower().count('e')
    except FileNotFoundError:
        # one of the error check is if the file is not found
        print("Error: The file does not exist")
        sys.exit(1) # sys.exit(1) will close the program with an error 
        #sys.exit(0) will close a program without an error
    except Exception as e: # getting if the program is interrupted by something else
        print(f'an error has occurred: {e}')
        sys.exit(1)

if len(sys.argv) != 2:
    print("Usage: python es.py <filename>")
    sys.exit(1)
filename=sys.argv[1]
if not os.path.isfile(filename) or not filename.endswith('.txt'):
        print("Error: Please provide a valid text file.")
        sys.exit(1)

e_count = count_es(filename)
print(e_count)
