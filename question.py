# Write a program to open three files 1.txt 2.txt & 3.txt. If any of these files are not present a message without exiting the program must be printed prompting the same
'''
def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")        

readFile('1.txt')
readFile('2.txt')
readFile('3.txt')

# Write a program to print third, fifth and seventh element from a list using enumerate function
list = [1, 3, "aditya", 4, 7, 6, 0.5]
for index, item in enumerate(list):
    if index==2 or index==4 or index==6:
        print(index, item)

# Write a list comprehension to print a list which contains the multiplication table of a user entered number:
a = int(input("Enter a number whose multiplication table you wish: "))
b = [a * i for i in range(1, 11)]
print(b)

# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ZeroDivisionError.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a/b
    print(f"{a}/{b}={c}")
    
except ZeroDivisionError as e:
    print("infinite")

#Store the multiplication table generated in quetion 3  in a file Table.txt
a = int(input("Enter a number whose multiplication table you wish: "))
b = [a * i for i in range(1, 11)]
print(b)
with open("Table.txt", "a") as f:
    f.write(str(b)) # we cannot put only b because write() argument must be str, not list:
    f.write('\n')
'''    
a = int(input("Enter a number whose multiplication table you wish: "))
b = [a * i for i in range(1, 11)]
print(b)