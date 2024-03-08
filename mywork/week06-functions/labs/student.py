#  function that prints out a menu of commands we can perform

def displayMenu():
    print("What would you like to do? :")
    print("\n(a) add a new student")
    print("\n(b) view student")
    print("\n(c) Quit")
    choice = input(" Input (a/b/c):"). strip()
    return(choice)

# test the function (it works)
# choice=displayMenu()
# print(f"your choice is {choice}")

def doAdd():
    print("in adding")

def doView ():
    print("in viewing")
choice= displayMenu()

while (choice!='q'):
    if choice == 'a':
     doAdd()
     
    elif choice =="v":
       doView()
choice=displayMenu()

students=[]

