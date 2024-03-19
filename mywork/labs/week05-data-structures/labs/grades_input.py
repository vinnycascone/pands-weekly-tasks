#created an empty list
student=[]

while True : 
    student_name=input('enter a student name: (leave blank to finish)').strip()
    #strip function that remove all blank space, investigate more string functions
    if not  student_name:
       break
    #otherwise collect the info of the modules
    #created another empty list inside the while
    modules=[]
    while True :
        module_name=input('enter a module name: (leave blank to finish)').strip() #empty brakets to remove empty spaces
        if not module_name:
            break
        grade_input=input(f'enter the grade for the module {module_name} ') #one grade for one module
        # let's check if it's a digit
        while not grade_input.isdigit(): #isdigit is the command to check if a string is a number
            print("Invalid grade. Please enter a number.")
            grade_input = input(f"Enter grade for {module_name}: ").strip()
        #convert the grade into an integer to store a grade as a number
        grade=int(grade_input)
        #put the info in the list modules
        modules.append({'courseName': module_name, 'grade': grade})
    student.append({'name': student_name,'modules' : modules})

for s in student:
 print(f"\nStudent: {s['name']}")
 for module in s['modules']:
        print(f"Module: {module ['courseName']} - Grade: {module['grade']}") 
