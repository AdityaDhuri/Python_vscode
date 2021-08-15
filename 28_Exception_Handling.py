#using try function for exception handling:
'''
while True:
    
    print("If you want to quit press 'q': ")
    a = input("Enter a number: ")     # if int used here will show error if input is enetered in letters
    if a == 'q' or a == 'Q':
        break

    try:
        a = float(a)     # using int here will wont show a error bcoz of using try using float will help you use decimal values.
        if a>6:
            print("number is greater than 6")
        else:
            print("number is smaller")    
    except Exception as e:
        print(f"Your input resulted in error{e}")

print("Thanks for playing")
'''

#Handling different exceptions:
try:
    a = input("enter a number: ")
    a = float(a)   #try without this and u'll find a error
    a = 1/a
    print(a)
#except Exception as e:   #this is universal/ancestor which shows all errror if inside try if we do not use float here and run the problem it shows error and valueError and Zeroerror will 
# not work because that  error does not comes in this both
#    print("error")    
except ValueError as e:   
   print("Please enter a valid value: ") 

except ZeroDivisionError as e:
   print("Please check if you are not dividing by zero: ")
print("Thanks")    