#write a program to greet using function:
'''
def greet(name="stranger"):
    print("Good day," + name)
greet("harry")    
greet("aditya")
greet()
'''
def factorial_rec(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_rec(n-1)
f = factorial_rec(3)
print(f)        
