# using property decorator:
'''
class Employee():
    country ='India'
    name = 'aditya'
    salary = 5000
    bonus =  500

    @property    
    def totalSalary(self):
        return self.salary + self.bonus

e = Employee()
print(e.salary)
print(e.totalSalary)
'''
# using setter
class Employee():
    country ='India'
    name = 'aditya'
    salary = 5000
    bonus =  500

    @property    
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self, val):
        #val = self.totalSalary
        self.bonus = val - self.salary

e = Employee()
print(e.salary)
print(e.totalSalary)
e.totalSalary=6000
print(e.bonus)