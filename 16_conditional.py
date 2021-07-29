# if-elif-else
'''
a = 10
if(a>10):
    print("a is greater than 10")
elif(a>2):
    print("a is greater than 2")
elif(a>5):
    print("a is greater than 5")    #only if(a>10) will execute here if it was false elif(a>2) will execute and so on 
else:
    print("ntng")

#to use multiple  or nested if
a = 20
if(a>10):
    print("a is greater than 10")
if(a>15):
    print("a is greater than 15")
elif(a>19):
    print("a is greater than 19")    
if(a>20):
    print("a is greater than 20")
else:
    print("a is not greater than 20")            

# Write a program to print to check if entered age is greater or less than 18 print older and younger resp 
a = int(input("Enter your age\n")) #bcoz age is integer
if (a>18):
    print("Older")
else:
    print("Younger")    

# Logical and Reasoning
a = int(input("Enter your age\n"))
if (a>20 and a<50):
    print("Can work")
else:
    print("Cannot work")
       
if (a>20 or a<15):
    print("Can work")
else:
    print("Cannot work")   

# in and is

a = 32
if(a is 320): # is or == if both values are same it prints yes else no
    print("yes")
else:
    print("no")    
a =[20, 15, 45]
b = 20
print(15 in a) #finds the number in the given list; if found gives answer true
print(b is 20) #if answer is same gives answer true
'''    
