'''SOLUTIONS'''


""" Q1> Create two virtual environments, install few packages in the first one. How do you create a similar environment in the secon one."""

# To create virtual environment write this on the terminal:-

virtualenv env1(environment_name)
virtual env2(environment_name)

# In order to activate any environment for example, I wish to activate env1 we will write:-

.\env1\Scripts\activate.ps1                   # This will activate the environment 

# In order to install any packages write:-
pip install pandas==1.5.2                     # This will specify the version of the pandas which is to be installed
pip install pyjokes

pip freeze > requirements_env1.txt              # This will create the txt file which will contain the names along with the version of the packages installed in the first environment

deactivate                                    # Deactivating the environment in neccessary

# And we will do the same for env2:-

.\env2\Scripts\activate.ps1                   # This will activate the environment

pip install pandas                            # This will install the latest version of pandas
pip install numpy==1.26.4

            #OR 
# If you wish to install from the previous environment then write:-

pip install -r .\requirements_env1.txt 

deactivate                                    # Deactivating the env2


""" Q2> Write a program to input name, marks and phone number of a student and format it using the format function in the following given format:
     " The name of the student is {student_name}, his marks are {Student_marks} and his phone number is {Phone_number}"."""

stu_name =input("Enter the name of the student: ")
stu_marks = float(input("Enter the marks of the student: "))
stu_phone_number = int(input("Enter the phone number of the student: "))

string = "The name of the student is {0}, his marks are: {1} and his phone number is: {2}".format(stu_name,stu_marks,stu_phone_number)

print(string)

# OUTPUT:-
Enter the name of the student: James
Enter the marks of the student: 99.9
Enter the phone number of the student: 9192631770
The name of the student is James, his marks are: 99.9 and his phone number is: 9192631770


""" Q3> A list contains the multiplicvation of 7. Write a program to convert it to vertical string of same numbers."""

table = [str(7*i) for i in range(11)]
s = "\n".join(table)
print(s)

# OUTPUT:- 
0
7
14
21
28
35
42
49
56
63
70


"""Q4> Write a program to filter a list of numbers which are divisible by 5."""

def divisible(n):
    if(n % 5 == 0):
        return True
    return False

l = [5,0,25,26,24,48,50,15,35,36]
print(f"The list is: {l}")
divisibleFIve = filter(divisible,l)
print("The numbers which are divisible by 5 in the given list are: ")
print(list(divisibleFIve))


"""Q5> Write a program to find the maximum of the numbers in a list using the reduce function."""

from functools import reduce

def max(a,b):
     if a > b:
          return a 
     return b

l = [5,0,25,26,24,48,50,15,35,36]
print(f"The maximum number from the given list{l} is: {reduce(max,l)}")


"""Q6> Run pip freeze for the system interpreter. Take the content and create a virtualenv."""

# First write pip freeze to look up on the installed packages on the global python 

# After seeing save them all to .txt file by running this code on the terminal:-
pip freeze > requirements_env1.txt

# Then create a new virtual environment:-
virtuaalenv env1

# Activate it:-
.\env1\Scripts\activate.ps1

# To download all the packages from the .txt file write this:-
pip install -r.\requirements_env1.txt

# It will take a while to install after installation deactivate the virtualenv by writing this:-
deactivate


"""Q7> Explore the 'Flask' module and create a web server using Flask and Python."""

