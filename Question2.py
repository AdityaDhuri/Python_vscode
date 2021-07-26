#Write a python program to display a user entered name followed by Good Afternoon using input() function
'''
a = input("Enter your Name:\n")
print("Good Afternoon", a) #diff ways to print
print("Good Afternoon," + a)

#Write a program to fill in a letter template given below with name and date
# letter = 'Dear <Name>
#                    you are selected!
#                   <Date>

#####letter = ' Dear <|name|>\n \tyou are selected!\n Date: <|Date|>'

letter = ''
Dear <|name|>,
Greetings from XYZ
You are selected
Date: <|Date|>
''
Name = input("Enter your name:\n")
Date = input("Enter date:\n")
letter = letter.replace("<|name|>",Name)
letter = letter.replace("<|Date|>",Date)
print(letter)

# Write a Program to detect double spaces in string
st = "This is a very lovely  day   ok"
doubleSpaces = st.find("  ")
print(doubleSpaces) 
#replace  doubleSpace with single space
st = st.replace("  "," ")
print(st) # if more than two space is present it will not replace them 
'''
#Write a program to format the foll letter using escape sequence character
letter ="Dear Aditya,This Python course is nice.Thanks!"
print(letter)
letter_formatted ="Dear Aditya,\nThis Python course is nice.\nThanks!" #letter = print("Dear Aditya,\nThis Python course is nice.\nThanks!")
print(letter_formatted) # it will also print but value is not stored in letter if print(letter) it will show none

