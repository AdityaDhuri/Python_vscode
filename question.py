# Write a program using function to find the greatest of three numbers:
'''
a = int(input("Enter a no: "))
b = int(input("Enter a no: "))
c = int(input("Enter a no: "))
def greatest(a, b, c):
    if (a>=b and a>=c):
        return a 
    elif (b>a and b>c): 
        return b   
    else:
        return c   
z = greatest( a, b, c)
print(f"The greater number is {z}")

#Write a program to convert celcius to farenheit:
a = int(input("Enter celcius to convert into farenheit: "))
def farenheit(a):
    a =  a * 9/5 + 32
    return a
f = farenheit(a)
print(f"Conversion of {a} Degree Celicus to Farenheit is {f}")    

#Write a recursive function to calculate the sum of first n narural no:
a = int(input("Enter a no: "))
def number(a):
    if (a <= 0):
        return 0
    return a + number(a-1)
z = number(a)
print("sum of " + str(a) + "is " + str(z))

#star
a = int(input("Enter a no: "))
for i in range(a):
    print("*" * (a-i))
 '''  
# inches to cm using function
a = int(input("Enter a number to convert from iches to cm: "))
def cm(a):
    a = a * 2.54
    return a
f = cm(a)    
print(f"conversion from iches to cm is {f}")
'''
#write a program to remove a given word from a string and strip it at the same time. using function
a = "      aditya bana bocha gadhav    "
def b(a, word):
    c = a.replace(word,"")
    return c.strip()
d = b(a,"bocha")
print(d)


#multiplication table using function:
a = int(input("Enter the number:\n"))
def multiplication(a):
    for i in range(1,11):
        print(a,'X', i, '=',a*i)  
multiplication(a)    
'''
words = '''
Hawkins Cooker Ltd. may be the best  start I can get for my carrier. As I read in your Bio, company gives well-established
management training which will help me to increase my skills and knowledge. I am starting my carrer as a python developer and i tend to reach the height, from where I can feel my success.
From your guidance and expertise i can make that happen within a short period of time. Debate, Drama, Sportsman, Mentor, Challenger, Team-Player, Quick-Learner, Analytical Thinking are
some of my skills. I am also hungry for work and if you give me an opportunity, I will be the best candidate selected for sure.
'''
print(len(words))