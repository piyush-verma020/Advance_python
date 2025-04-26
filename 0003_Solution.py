# Q3> Write a list comprehension which will print the multiplication table of the user entered number.

numbers : list = []
for i in range(5):
    value = int(input("Enter the integer values of the list: "))
    numbers.append(value)

for num in numbers:
    table : list = [num * i for i in range(1, 11)]
    print(f"\nMultiplication table of {num}:")
    for i, val in enumerate(table, start=0):
        print(f"{num} x {i} = {val}")
