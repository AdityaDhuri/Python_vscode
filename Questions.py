# Create two virtual environment and install few packages in the first one. how do you create a similar environment in the second one?

#   to create a virtual environment we have to install a virtual environment.
#   step 1: pip install virtualenv
#   step 2: activate => virtualenv myproj1env 
#   #step 3: in terminal => .\myproj1env\Scripts\activate.ps1  ( in case of error type => Set-ExecutionPolicy -ExecutionPolicy Unrestricted and then step 3)
#   this is how one virtualenv is created. To create multiple follow from step 2
#   this will show name of your virtualenv in your terminal as (myproj1env) PS A:\
#   After creating 1st virtual env add some contents in it like : pip install flash(this is only a eg.)
#   myproj1env will have this flash installed in it
#   To find out all contents inside it type => pip freeze
#   To copy your requirement/contents to another file use => pip freeze > requirements.txt (all contents will be copied in requirements.txt)   
#   To install contents of myproj1env to myproj2env first deacativate it by typing deactivate in terminal then open second terminal  add requirements.txt in that terinal
#   and type => pip install -r requirements.txt
#   using this command will install all the contents from requirements.txt
'''
# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is aditya, his marks are 92 and phone number is 9999988888"
name = input("Enter your name: ")
marks = int(input("Please Enter your Marks: "))
num = int(input("Please enter your mobile number: "))
a = "The name of the student is {}, his marks are {} and phone number is {}.".format(name, marks, num)
print(a)

# A List contains the multiplication table of 7. Write a program to convert it to a vertical string of same number(7)
#                                                                                                                 (14)
#                                                                                                                 (21)
l = [str(i*7) for i in range(1, 11)]
print(l)
v ="\n".join(l)
print(v)

# Write a program to filter a list of numbers which are divisible by 5
l = [1, 5, 10, 12, 15, 25, 20]
g = lambda num: num%5 == 0 
print(list(filter(g, l)))   

#Write a program to find the maximum of the numbers in a list using the reduce function:
from functools import reduce
l = [3, 8, 4, 5, 10]
a = reduce(max, l)   #max is a inbuilt function
print(a)

# Explore the Flask module and Create a web server using Flask and Python. 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World Skealy is back.'

if __name__== "__main__":
    app.run(debug=True)
'''    
from functools import reduce
l = [3, 8, 4, 5, 10]
a = reduce(min, l) 
print(a)