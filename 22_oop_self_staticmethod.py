# use of self and @staticmethod in class:

#1 self
class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary of this employee in {self.company} is {self.salary}")

#2 @staticmethod     this is used in case user dont want self
    @staticmethod
    def greet():
        print("Good morning, Sir")
harry = Employee()
harry.salary = 1000000 #adding value in the class
harry.getsalary() #Employee.getsalary(harry) this is what that means.asg
harry.greet()
