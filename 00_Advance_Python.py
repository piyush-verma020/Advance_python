"""ADVANCED PYTHON"""

'''Some python operators and their syntax'''


# Walrus Operators

if(n := len([1,2,3,4,5])) > 3:
    print(f"List is too long, ({n} elements, expected <= 3)")


# Variable type hint

age : int = 25
# Function type hint
def greeting(name:str) -> str:
    return f"Hello, {name}"
# Usage
print(greeting("Gita"))


# Match case which is similar to the switch case in another porgraming languages

while(True):
    choice = int(input("Enter a number between 1 and 3: "))
    match choice:
        case 1:
            print("You have a draw")
        case 2:
            print("We have a winner!")
            break
        case 3:
            print("LOOSER!!")
        case _:
            print("INVALID INPUT!!")
            break


# Dictionary merging

dict1: dict = {'a' : 1, 'b' : 2}
dict2: dict = {'b' : 3, 'c' : 4}
merged = dict1 | dict2
print(merged)


# Syntax for opening two different files at the same time

with(
    open("File1.txt") as f1,
    open("File2.txt") as f2
):
    r1 = f1.readline()
    r2 = f2.readline()
print(r1,"\n",r2)


# Exception Handeling

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
print("THANK YOU")


# Try with some exceptional errors

try:
    a = int(input("Enter the value of numerator: "))
    b = int(input("Enter the value of denominator: "))
    div = a / b
    print(f"The division of the two given number {a} / {b} is: {div}")
except ZeroDivisionError as z:
    print("Our code was not made to divide any number by zero!")
except ValueError as v:
    print(f"Well the input are meant to be numbers not str{v}")
print("Thank you")


# Try with else

try:
    a = int(input("Enter the value of numerator: "))
    b = int(input("Enter the value of denominator: "))
    div = a / b
    print(f"The division of the two given number {a} / {b} is: {div}")
except ZeroDivisionError as z:
    print("Our code was not made to divide any number by zero!")
    print("Please try again later!")
except ValueError as v:
    print(f"Well the input are meant to be numbers not str {v}")
    print("Please try again later!")
else:
    print("Thank you")        # This will only get executed only when there are no exceptions found i.e when the try block runs successfully


# Try with Finally

try:
    a = int(input("Enter the value of numerator: "))
    b = int(input("Enter the value of denominator: "))
    div = a / b
    print(f"The division of the two given number {a} / {b} is: {div}")
except ZeroDivisionError as z:
    print("Our code was not made to divide any number by zero!")
except ValueError as v:
    print(f"Well the input are meant to be numbers not str{v}")
finally:
    print("Thank you") # This will run regardless of any exception found or any eroor!


# Enumerate Function

l = [3, 535, 655, 984, 216, 56, 562]
for index, item in enumerate(l):
    print(f"The item at index number {index} is: {item}")


# List Comprehension

l1 = [1, 3, 5, 7, 9, 11]
l2 = [i for i in l1]
print(l2)       # This prints the list l2 which was copied from the exissting list
squared_list = [i*i for i in l1 if i <10]
print(squared_list)     # This will copy the list from l1 and prints the squared number of the each integer data which is lesser than 10
