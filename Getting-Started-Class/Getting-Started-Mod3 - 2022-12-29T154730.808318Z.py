# Module 3: Types, Statements, and other goodies
# *********************************************************
# *********************************************************

# Functions
# *****************************************************
# Best to have a function do a single task

"""
Function Notes
examples of funtions
    print()
    str()
    int()
"def" defines a function, Function Name, () what arguments get passed in
return *, will return a var out of the function
def sample(*arg) # will accept anything in a var called "arg", multiple args separated by ,
# Can also define arg when passing in
function_name(name="TJ", age=90)
def sample(**kwarg), will accept anything in a var called "kwarg", multiple args separated by ,
function_name(name="TJ", grade=90, location="NJ")
print(kwarg["name"], kwarg["grade"]), kwarg["location"]

"""

students = []
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)

another_student = input("Add a new student? (y/n) :")

while another_student == "y":
    student_name = input("Enter Student Name :)")
    student_id = input("Enter Student ID :")
    add_student(student_name, student_id)
    another_student = input("Add another student? (y/n) :")

student_list = get_students_titlecase()

print_students_titlecase()


