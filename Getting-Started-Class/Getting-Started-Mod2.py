# Module 2: Types, Statements, and other goodies
# *********************************************************
# *********************************************************

# Integers and Floats
# *****************************************************

"""
Multi Line Comment
"""

answer = 42  # Int
pi = 3.141592653589793  # Float
name = "Python"
machine = "HAL"
"Nice to meet you {0}.  I am {1}".format(name, machine)
f"Nice to meet you {name}.  I am {machine}" # Compressed way to write

#Boolean and None
#True/False
# *****************************************************

python_course = True # Sets Boolean var to True (First Char must be cap)
java_course = False
int(python_course) == 1 # Converts to Int and tests with Int
int(java_course) == 0
str(python_course) == "True" # Tests Boolean with String
aliens_found = None  # declaired var set to null

#Convert and Strings
# ******************************************************
# Integers and Floats

answer = 42
name = "Python"
pi = 3.141592653589793

#Convert and Strings
int(pi) # should convert to == 3
float(answer) # should convert to == 42.0
'Hello' == "Hello" == """Hello"""
"hello".capitalize() =="Hello"
"Hello".replace("e", "a") =="Hallo"
"hello".isalpha() == True # Checking to see if alpha char
"123".isdigit() == True # Checking to see if they are digits


# If Statement
# ********************************************************

number = 55
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")

if number:  # Number has a value (therefor True)
    print("Number is defined and truthy") 

text = "Python"
if text:
    print("Text is defined and truthy")

number = 5
if number != 5:  # Can use ==, !=, <=, >=, etc..
    print("Number is 5")
else:
    print("Number is not 5")

number = 5
if number != 5 and aliens_found: # "and" (both must be true/false), "or" one must be true or false
    print("Number is 5")
else:
    print("Number is not 5")
   
a = 1; b = 2  # "";"" will combine commands on one line
"bigger" if a > b else "smaller" # Compressed If/Else Statement

# Lists    Just like array but can be mixed int, string, float
# ***********************************************************

student_names = ["Jake", "Coby", "Kailey"]
print(student_names[0]) # 0 will get the first entry
print(student_names[2]) # to get the last entry, use -1
student_names.append("Todd") # appends to the end of the list
"mark" in student_names  # check for name in list
len(student_names)
del student_names[4] # deleted an element from list

#  List Slicing 
# student_names[1:-1] will skip the first and last entry
# ***********************************************************

x = 0
for index in range(10):  #range(5, 10, 2) Start/End/add, index just looping
    x += 10
    print("The value of X is {0}".format(x))

student_names = ["Jake", "Coby", "Kailey"]
for name in student_names :
    print("Currently testing " + name)
    if name == "Todd" :
        print("Found him! " + name)
        # break/continue could get out once item is found or continue

x = 0
while x < 10 :
    print("Count is {0}".format(x))
    x +=1 # must add/subtract one to counter in while loops

# Dictionaries
# *************************************************************
student = {
    "name": "TJ",
    "student_id" : 21,
    "feedback" : None
} # Curly brackets for single items, can be put on one line, need :

all_student = [
    {"name": "Coby", "student_id" : 21},
    {"name": "Kailey", "student_id" : 22},
    {"name": "Jake", "student_id" : 23}
] # notice the brackets for multiple items

# Methods
student.get("name")  # Using the get Method to pull the student name
# student.value("student_id") # Using the value Method, will return dic value
del student["Name"]

# Exceptions
# **********************************************************
student = {
    "name": "TJ",
    "student_id" : 21,
    "feedback" : None
} # Curly brackets for single items
student["last_name"] = "Totland" # appends dic item/value

try:
    last_name = student["last_name"]
except KeyError: # Looking for key errors
    print("Error finding last_name")
except TypeError as error: # Looking for type errors
    print("I cannot add these 2 together") # When adding str and int together
    print(error) # Will print error message
except Exception: # Just about any error
    print("Unknown Error")
print("This code executes!")

# Other Data Types
# **********************************************************
'''
complex # Complex numbers
bytes 
bytearray
tuple # Cannot change variable
setfrozen
set ()
'''

