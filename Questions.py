#Write a program to find the greatest of four no entered by the user

a = int(input("Enter first no:\n"))
b = int(input("Enter 2nd no:\n"))
c = int(input("Enter 3rd no:\n"))
d = int(input("Enter 4th no:\n"))
''' way 1 of my own
if (a>b and a>c and a>d):
    print("greater no is", a)
elif (b>a and b>c and b>d):
    print("greater no is", b)
elif (c>a and c>b and c>d):
    print("greater no is", c)
else:
    print("greater no is", d)            
'''   
if(a>b):
    x = a
else:
    x = b
if(c>d):
    y = c
else:
    y = d
if(x>y):
    print(x, "is greatest")
else:
    print(y, "is greatest")

# Write a program to find out whether a student is passed or failed; if it requires total 40% and atleast 33% in each subject to pass. Assume 3 sub and take marks from user
x = (input("Enter name of 1st student:\n"))
a = int(input("Enter English subject marks:\n"))
b = int(input("Enter Maths subject marks:\n"))
c = int(input("Enter science subject marks:\n"))
#y = (input("Enter name of 2nd student:\n"))    for 3 users
#d = int(input("Enter English subject:\n"))
#e = int(input("Enter Maths subject:\n"))
#f = int(input("Enter science subject:\n"))
#z = (input("Enter name of 3rd student:\n"))
#g = int(input("Enter English subject:\n"))
#h = int(input("Enter Maths subject:\n"))
#i = int(input("Enter science subject:\n"))
if (a<33 or b<33 or c<33 ):
    print("you are failed in one of the subject",x)
elif (a + b +c)/3 <40:
    print("you are failed",x)   
else :
    print("Congrats! You are passed",x)   
#if (d<33 or e<33 or f<33 ):
#    print("you are failed in one of the subject",y)
#elif (d + e + f)/3 <40:
#    print("you are failed",y)   
#else :
#    print("Congrats! You are passed",y)   
#if (g<33 or h<33 or i<33 ):
#    print("you are failed in one of the subject",z)
#elif (g + h + i)/3 <40:
#    print("you are failed",z)   
#else :
#    print("Congrats! You are passed",z)            

# A spam comment is defined as a text conatining following keywords: "make a lot of money", "buy now", "subscribe now", "click this". Write a program to detect this spam.

a = input("Enter text\n")

if("make a lot of money" in a):
    spam = True
elif("buy " in a):
    spam = True
elif("subscribe " in a):
    spam = True
elif("click this" in a):
    spam = True  
else:
    spam = False
if (spam):
    print("This is a spam")
else:
    print("This is not a spam")  

# Write a program to find a given username contains less than 10 characters or not:

name = input("Enter your name:\n")
a = len(name)
print(a)
if(a < 10):
    print("Your name consist less than 10 character")
else:
    print("Your name consist more than 10 character")    
  
# Write a program to find out whether a given name is present in a list or not

a = input("Enter a name:\n")
b = ["aditya", "bana", "bocha"]
if (a in b):
    print("the name is present")
else:
    print("the name is not present")    

# Write a program to calculate the grade of a student from this marks from the foll: 90-100=Ex ; 80-90=A ; 70-80=B ; 60-70=C ; 50-60=D ; below 50=E
a = int(input("Enter your marks:\n"))
if(a>=90 ):
    print("Your grade is Excellent")
elif(a>=80 ):
    print("Your grade is A")
elif(a>=70 ):
    print("Your grade is B")
elif(a>=60 ):
    print("Your grade is C")    
elif(a>=50 ):
    print("Your grade is D")
else:
    print("Your grade is F")    

# Wite a program to find out whether the post is talking about Bana
a = ("Name of BaNa is Bocha")
if 'bana' in a.lower():  #if letters used all small type lower all capital use upper
    print("the name is present")  
else:
    print("the name is not present")      
