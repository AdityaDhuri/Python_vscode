# Write a program to create a dictionary of Hindi words with values as their english translation. Provide user with an option to look it up

a = {
    "suraj": "sun",
    "chand": "moon",
    "thaile": "bag",
    "pagal": "mad"
}
print("Options are",a.keys()) #to give all keys to the user
b = input("Enter the word you want to search\n")
#print("The meaning of your word is",a[b]) this line will give error if the word entered is not present
print("The meaning of your word is",a.get(b)) #get does not give error but remember to put () instead of []

# Write a program to input eight no from the user and display all the unique(no repeated value should be printed) numbers once

a = int(input("Enter no 1st\n")) #if without int done it will show the entered no but as string and not indexed
b = int(input("Enter no 2nd\n"))
c = int(input("Enter no 3rd\n"))
d = int(input("Enter no 4th\n"))
e = int(input("Enter no 5th\n"))
f = int(input("Enter no 6th\n"))
g = int(input("Enter no 7th\n"))
h = int(input("Enter no 8th\n"))
no = {a, b, c, d, e, f, g, h}
print(no)

#can we have 18=integer and 18=string as a value
s = {18, "18", 18}
print(s) #in a set you cannot print same number only if they are of different type

#What will be the length of following set s: 

s = set()
s.add(20)
s.add(20.0)
s.add("20")

s = set() # this is an empty set
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) #20.0 and 20 are considered same and not on their type

#s = {} what is it type
s = {}  #this is not an empty set this is a empty dictionary
print(type(s))

# Create an empty dicitonary. Allow 4 friends to enter their favourite language as values and use keys as thie name. Assume that name are unique(diff)
s = {}
a = input("Enter your name\n")
w = input("Enter your favourite language\n")
b = input("Enter your name\n")
x = input("Enter your favourite language\n")
c = input("Enter your name\n")
y = input("Enter your favourite language\n")
d = input("Enter your name\n")
z = input("Enter your favourite language\n")
#s.update({a : w}) 
#s.update({b : x})
#s.update({c : y})
#s.update({d : z})
s[a] = w # if used quote for a like ('a') it will be a string and a will  be printed
s[b] = x
s[c] = y
s[d] = z
print(s)

##what happens if the above program has 2 same name
# it will replace with the new language for the first name . keys are never to be same

##what happens if the above program has 2 same language
#no change . it prints all . values can be same

##can we change the values inside set...
# no set is hashable