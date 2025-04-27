"""Some of the codes which includes pip will only run on the terminal"""


# # To create a virtual environment write:

# pip install virtualenv


# # To give name to an environment write:

# virtualenv environment_name


# # To see all of the downloaded python packages write:

# pip freeze


# # To store all the names and the version of all downloaded python packages write:

# pip freeze > file_name.txt


# # To download or install all the modules from an existing text file write:

# pip install -r .\file_name.txt 


# # Lambda Function

# square = int(input("Enter the number whose square you wish to see: "))
# value= lambda x : x*x
# print(value(square))


# # Join method

# l = ["apple", "bananna", "pineapple"]
# result = " :: ".join(l).capitalize()
# print(result)


# # Format Method

# a = "{} is a good {}".format("Govt", "dog")
# b = "{1} is a good {0}".format("Govt", "dog")

# print(a)
# print(b)


# # Map, Filter and Reduce

# # MAP

# from functools import reduce

# l = [1,2,3,4,5]
# square = lambda x:x*x
# sqlist = map(square,l)
# print(l)
# print("The squared of the given list is: ")
# print(list(sqlist))
# print("\n")

# # FILTER

# def even(n):
#     if(n%2 == 0):
#         return True
#     return False

# onlyEven = filter(even,l)
# print("The only Even number in the given list are: ")
# print(list(onlyEven))
# print("\n")

# # REDUCE

# def sum(a, b):
#     return a + b
# print("The sum of the given list is: ")
# print(reduce(sum,l))
# print("\n")
