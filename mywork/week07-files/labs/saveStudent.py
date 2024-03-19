# function that prints out a menu of command

import json
def displayMenu():
    print('What would you like to do?')
    print('a) add a new student')
    print('v) view student')
    print('s) save student')
    print('l) load student')
    print('q) Quit')
    choice= input('Please input one of the letter a, v, s, l, q : \t').strip()
    return choice

#function that reads the module

def read_modules():
    modules=[] #empty list of modules
    moduleName= input("\tEnter the first moduleName (blank to quit) :").strip() #if put a blank never enter the while

    while moduleName != "": #now we have a name and we go inside the while 
        module= {} #empty dictionary
        module['name']= moduleName 
        module['grade']=int(input("\t\t Enter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit):").strip() #going back to the while as module name is not empty


    return modules # returning an empty list to test our function
    


#function that adds the choice
def do_add(stu):
    print('we are in adding section')
    current_student={} # create empty dictionary
    current_student["name"]= input('enter name : ') #create the variable outside to input info to empty dict
    current_student["modules"] = read_modules()
    stu.append(current_student) #adding the info to the students list


def display_module(modules):
    print ("\tName  \tGrade")
    for module in modules: 
        print(f'\t{ module["name"]}  \t{ module["grade"]}')
def do_view(stu):
    for currentStudent in stu: 
        print(currentStudent["name"]) 
        display_module(currentStudent["modules"])

def writeDict(obj): 
    with open('student.json', 'wt') as f: 
        json.dump(obj,f) 

def do_load (): 
    with open('student.json') as f:
        return json.load(f)

def do_save(stu):
 print(f'we are inside do_save')
 writeDict(students) 
 print("students saved")
#create the variable to store the students:
students=[] #empty list



#calling the function displayMenu which is returning the value choice
choice=displayMenu()
print(f' your choice is {choice}')

#creating the loop until the user inputs q
while choice != 'q':
    if choice == 'a': #we call the function
        do_add(students)
    elif choice == 's':
        do_save(students)
    elif choice == 'v':
        do_view(students)
    elif choice=='l':
        students=do_load()
    elif choice != 'q': 
        print('\n\n please select a, v, q ')
    choice=displayMenu() 
        
#creating the variable student to store the info