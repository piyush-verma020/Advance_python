# Q2> Write a program to print third, fifth and seventh element from a list using enumerate function.

l : list =[]
for i in range(10):
    list_value = input(f"Enter the values of the list at index {i}: ")
    l.append(list_value)
for index, item in enumerate(l):
    if(index in (2,4,6)):
        print(f"The elements in position {index} is: {item}")
