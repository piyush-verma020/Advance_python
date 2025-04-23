# Q1> Write a program to open three files 1.txt, 2.txt and 3.txt if these files are not present
#     a message without exiting the program must be printed prompting the same.


try:
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")
    file3 = input("Enter the name of the third file: ")
    with (
        open (file1) as f1,
        open(file2) as f2,
        open(file3) as f3,
    ):
        r1 = f1.readline()
        r2 = f2.readline()
        r3 = f3.readline()
        print(r1)
        print(r2)
        print(r3)
except FileNotFoundError as f:
    print("There are no files existing with these names")
