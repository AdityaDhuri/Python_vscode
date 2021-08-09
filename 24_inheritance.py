#inheritance / single-inheritance

class Employee(): #this is the main class/ parent class:
    company = 'Google'

    def getStatus(self):
        print(f"The employee is working in {self.company}")
    
class Programmer(Employee): # we can defined two class. this is the child class 
    language = 'python'

    def lang(self):
        print(f"The eployee is specalized in {self.language}")


a = Employee()
a.getStatus()
b = Programmer()
b.lang()

#multiple inheritance:
class Employee():
    company = 'visa'

class Freelancer():
    company = 'Fiverr'

class Programmer(Employee, Freelancer):
    name = 'Rohit'

p =Programmer()
print(p.company)    

#MultiLevel inheritance:
class Person():
    country = 'India'
    def __init__(self):
        print(f"I work in {self.country}")

    def takeBreath(self):
        print("I am Breathing")

class Employee(Person):
    language = 'python'
    company = 'Google'

    def __init__(self):
        super().__init__()
        print(f"I work in {self.company}")
        
    def getSalary(self):
        print(f"Employee work in {self.company} and knows {self.language}")
    
    def takeBreath(self):
        print("I am Breathing now")    

class Programmer(Employee):
    company = 'Fiverr'
    def getSalary(self):
        super().getSalary()
        print(f"No salary to the programmers in {self.company}")

#p = Person()
#E = Employee()
Pr = Programmer()
#Pr.getSalary()
print(takeBreath)
