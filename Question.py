# Create a class programmer for storing information of few programmers working at microsoft:

class programmer():
    company = "Microsoft"
    def __init__(self, name, product):
        self.name  = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and he/she is working on product {self.product}")    

a = programmer("harry", "skype")
b = programmer("alka", "GitHub")
a.getInfo()
b.getInfo()

# Write a class capable of finding square, square root, cube of a number.
a =  int(input("Enter a number to find its Square , Cube and Square root: "))

class calculator:
    def __init__(self, number):
        self.number = number
        
    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")

    def squareRoot(self):
        print(f"The squareRoot of {self.number} is {self.number **0.5}")   

b = calculator(a)
b.square()
b.cube() 
b.squareRoot()    

#Create a class with a class attribute a; Create an object from it and set a directly using object a=0. does this change the class attribute?

class sample():
    a = "Harry"
obj = sample()
obj.a = "vicky"   # this is a instant attribute...value given directly after creating class
#sample.a = "vicky"  this will change the class attribute
print(sample.a)   # this will print the value that is given in class
print(obj.a)      # this will print the instant value...
# therefore the value of a will not change in class

# Add a static method  to greet the user:
class name():
    @staticmethod
    def greet():
        print("Hello Good Morning, Sir")
a = name()
a.greet()

# Write a class Train which will have methods to book a ticket, get status(no of seats) and get fare information of trains running under Indian Railway:

a =  input("Enter the name of the train you have selected: ")
b =  input("Enter the destination: ")


class Train():
    def __init__(self, name, ticket, cost, status):
        self.name = name
        self.ticket = ticket
        self.cost = cost
        self.status = status
    def getstatus(self):
        print(f"Your train for the journey is {self.name}")
        print(f"The selected Destination is {self.ticket}")
        print(f"The cost of your journey till {self.ticket} will be {self.cost}")    
    def seats(self):    
        print(f"The status of your train (the no of available seats is) {self.status} ")    
    def Booking(self):
        if(self.status>0):
            print(f"Your ticket has been booked! Your seat no is {self.status}")
            self.status = self.status - 1    
        else:
            print("Sorry this Train is Booked! KINDLY TRY IN TATKAL")
    

a = Train(a, b, 250, 1)
a.getstatus()
a.seats()
a.Booking()
a.Booking()

# what is we use slf instead of self :
class programmer():
    company = "Microsoft"
    def __init__(self, name, product):   # using slf will run the program and aslo give the output but will show problem but wont show error
        self.name  = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and he/she is working on product {self.product}")    

a = programmer("harry", "skype")
b = programmer("alka", "GitHub")
a.getInfo()
b.getInfo()
 