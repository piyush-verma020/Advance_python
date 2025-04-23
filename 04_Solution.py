# Q4> Write a program to display a/b where a and b are integers if b = 0 then display infinity by handling the 'ZeroDivionError'.

try:
    a = int(input("Enter the value of numerator: "))
    b = int(input("Enter the value of denominator: "))
    div = a / b
    print(f"The division of the two given number {a} / {b} is: {div}")
except ZeroDivisionError as z:
    print("Our code was not made to divide any number by zero!")
    print("Please try again later!")
except ValueError as v:
    print(f"Well the input are meant to be numbers not str which is an {v}")
    print("Please try again later!")
finally:
    print("Thank you")