# Q5> Store the multiplication table generated in problem 3 in a file named 'table.txt'.


numbers = []
for i in range(5):
    value = int(input("Enter the integer values of the list: "))
    numbers.append(value)

for num in numbers:
    table = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
    print(f"\nMultiplication table of {num}:")
    for line in table:
        print(line)
    with open(f"table/table_{num}.txt", "w") as f:
        f.write("\n".join(table))
        
# OR

n = int(input("Enter a number whose table you wish to see: "))

table : list = [n * i for i in range(0,11)]
with open("tables.txt", "a") as f:
    f.write(f"Table of {n} is: {str(table)} \n")
