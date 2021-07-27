# Write a program to store seven fruits in a list entered by the user
'''
a = input("Enter 1st fruit name:\n ")
b = input("Enter 2nd fruit name:\n ")
c = input("Enter 3rd fruit name:\n ")
d = input("Enter 4th fruit name:\n ")
e = input("Enter 5th fruit name:\n ")
f = input("Enter 6th fruit name:\n ")
g = input("Enter 7th fruit name:\n ")
fruits = [a, b, c, d, e, f, g]
print(fruits)
'''
#Write a program to accept marks of 6 student and diplay them in a sorted manner

print("Please Enter your Marks:\n")
a = int(input("Marks of 1st student:\n")) # ("string") so convert into integer
b = int(input("Marks of 2nd student:\n"))
c = int(input("Marks of 3rd student:\n"))
d = int(input("Marks of 4th student:\n"))
e = int(input("Marks of 5th student:\n"))
f = int(input("Marks of 6th student:\n"))
print("Marks of 6 students are as follow:\n")
Marks = [a, b, c, d, e, f]
Marks.sort()
print(Marks)
'''
#Check that a tuple cannot be changed in python

a = (2, 8, 10, 12, 16)
#a[2] = 4
print(a)

#Writw a program to sum a list with 4 numbers:

a = [20, 40, 60, 80]
print(a[0] + a[1] + a[2] + a[3])
print(sum(a)) #alternate method it gives sum of all the numbers

#Write a program to count the numbers of zeroes in the following tuple a = (7, 0, 8, 0, 0, 9) and find position of 8

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
print(a.index(8))
'''