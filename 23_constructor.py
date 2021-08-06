class Employee:
    company = "Google"
    def getsalary(self, signature):
        print(f"salary of this employee in {self.company} is {self.salary}")


    def __init__(self, name, salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
   
    def getDetails(self):
        print(f"Salary for {self.name} working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning, Sir")

harry = Employee("harry", 100000, "Youtube") 
#harry = Employee() will give error bcoz the values inside are not given
harry.getDetails()