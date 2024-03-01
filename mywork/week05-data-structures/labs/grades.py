# stores student name and list of courses and grades in a dict
# print out the data
# the number of course could change

student= {
   'name' : 'Mary',
   'modules':[{'course_name': 'Math' , 'grade':95},{'course_name': 'History' , 'grade':90}, {'course_name': 'Geo' , 'grade':89}]

}
print(f"Student: {student['name']}")
for m in student['modules']:
    print(f"\t {m['course_name']} : {m['grade']}")


