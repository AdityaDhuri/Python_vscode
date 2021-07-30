#write a program to print multiplication table of a given number using for loop
'''
a = int(input("Enter the number whose multiplication table you want to see:\t"))
for i in range(1, 11):
    print(str(a) + " x " + str(i) + " = " + str(a*i))
    #print(f"{a}X{i}={a*i}")

#Write a program to greet all the person names stored in a list L1 and which starts with A: L1 = ["Aditya","bana","ankita","Aquib","navneet"]    
L1 = ["Aditya","bana","ankita","Aquib","navneet"]
for name in L1:
    if name.startswith("A"):
        print("Greetings " + name)

# write a program to print multiplication table of a given number using while loop:
a = int(input("Enter the number whose multiplication table you want to see:\t"))
i = 1
while (i<11):
    print(str(a) + " x " + str(i) + " = " + str(a*i))
    i = i + 1

# Write a program to find out if a entered number is prime or not
'''
number = int(input("Enter the number: "))
prime = True
for i in range(2, number):
    if (number%i == 0):    # % gives remainder in integer form. 
        prime = False
        break
if prime:
    print("this is a prime no")
else:
    print("not a prime no")
'''
#Write a program to find the sum of n natural number using while loop:
a = int(input("enter the no till u want the sum "))
i = 0
b = 0
while (i<=a):
    b = b + i
    i = i + 1
print(b)

#Write a program to calculate the factorial of agiven number usimg for loop:

a = int(input("enter the number to be factorial: "))
b = 1
for i in range(1, (a+1)):
    b = b*i
print(f"The factorial of {a} is {b}")    #print(f" {}  {} ") f helps us to print inbetween values using a curly bracket

# Write a program to print the following star pattern: here n = 3
#     *
#   * * * 
# * * * * * 
a = int(input("Enter num: "))
for i in range(a):
    print(" " * (a-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (a-i-1))
 
#extra print to find 
a = int(input("Enter num: "))
for i in range(a):
    print(" " * (a-i-1), end="")
    print("*" * (i+1))   
for i in range(a):
    print(" " * (i+1), end="")
    print("*" * (a-i-1))

# Write a program to print the following star pattern: here n = 3
#  ***
#  * *
#  ***
num = int(input("enter no:"))
for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 or j==num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()            

# print multiplication table in reversed order using for loop:
a = int(input("Enter num: "))
for i in range(10,0,-1):
    print(f"{a}x{i}={a*i}")
   
for row in range(0, 6):

    for col in range(0, 7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*", end="")
        else:
            print(" ", end="")
    print()            
'''
#to print diamond
a =  int(input("Enter a no: "))
for i in range(a):
    print(" " * (a-i-1),end="")
    print("*" * (2*i+1))
for i in range(a):
    print(" " * (i+1),end="")
    print("*" * (2*a-2*i-3))
