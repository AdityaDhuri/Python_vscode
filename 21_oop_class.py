# use of class 
class Employee:
    company = "Google"
    salary = 200

harry = Employee()
harry.increment = 25 # adds increment in the class
#harry.salary = 300 #instance attribute
print(harry.company)
Employee.company = "youtube"   #changing the inside info in class
print(harry.company)
print(harry.salary)