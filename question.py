# Create  aclass C-2d Vector and use it to create another class representing a 3d  vector
'''
class C2dVector():
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"    

class C3dVector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k" 

c2d = C2dVector(1, 3)
c3d = C3dVector(1, 3, 7)
print(c2d)
print(c3d)

#Create a class pets from a class animals and further create class Dog from pets. add a method bark to class Dog:

class Animals():
    lion = 'Roar'
    Dog = 'humming'
class Pets(Animals):
    cat = 'meow'

class Dogs(Pets):
    @classmethod
    def changeName(self, b):
        self.Dog = b
    
a = Animals()
p = Pets()
d = Dogs()
print(d.Dog)
d.changeName('Bark')
print(d.Dog)

# Create a class Employee and add Salary and increment properties to it. 
# Write a method salary after Increment with a @property decorator with a setter which changes the value of increment based on the salary

class Employee():
    salary = 1000
    increment = 1.5

    @property
    def totalSalary(self):
        print("The salary of the Employee 1 is: ")
        return self.salary * self.increment
        
    @totalSalary.setter
    def totalSalary(self, final):
        self.increment = final / self.salary
        print("The increment in the Employee's 1 salary is: ")

e = Employee()
print(e.totalSalary)
e.totalSalary = 2000
print(e.increment)

#Write a class Complex to represent coplex numbers along with overloaded operators + and * which adds and multiplies them:
# (a+bi)(c+di) = (ac-bd) + (ad+bc)i
class ComplexNumber():
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return ComplexNumber(self.real + c.real, self.imaginary + c.imaginary)    
    
    def __mul__(self, c):
        mulReal = self.real * c.real - self.imaginary * c.imaginary
        mulImg = self.real * c.imaginary + self.imaginary * c.real
        return ComplexNumber(mulReal , mulImg)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(1, -2)
c2 = ComplexNumber(8, -3)
print(c1 +c2)
print(c1 * c2)

# Writw a class vector representing a vector of n dimensions. overload the + amd * operator which calculate the sum and the dot prduct of them:
class Vector():
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i  in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i  in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1 = Vector([1, 4])
v2 = Vector([1, 6])
print(v1 + v2)
print(v1 * v2)

#Write a __str__() method to print the vector 7i^ + 8j^ +10k^ assume vector of 3D:
class Vector():
    def __init__(self, i, j, k):
    #def __init__(self, vec):
        #self.vec = vec
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
        #return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

c1 = Vector(7, 8, 10)
#c1 = Vector([7, 8, 10])
print(c1)

#Overide the __len__() method on Vector of problem 5 to display the dimension of the vector.
class Vector():
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i  in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i  in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)   #this will print the length 

v1 = Vector([1, 4])
v2 = Vector([1, 6])
print(len(v1))
print(len(v2))
'''