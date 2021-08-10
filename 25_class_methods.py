#to chanege the class attribute we use @classmethod:

class Employee():
    country ='India'
    name = 'aditya'

    #def changeName(self,b):
    #   self.__class__.name = b   this is also a way to change the class attribute
    @classmethod    #using @classmethod will change the object inside class attribute
    def changeName(cls,b):
        cls.name = b
e = Employee()
print(e.name)
e.changeName('bana')
print(e.name)
print(Employee.name) #this will show what is originally inside the class. As we change class attribute here the value shows here is the value changed inside the class.

