#slicing

greeting = "Good Morning,"
name = " aditya" #adding space between double quotes will give u space in your output
print(type(name))
c = greeting + name
print(c)

# finding length of string by  slicing  positive and negative both ways
name = "aditya" 
print(name[1]) # []gives you the letter in  the position starting from 0 to length of your input string
print(name[0:3]) # [0:3] means upto 2 like (0,1,2)
# print(name[6]) as position 6 does not exist here
print(name[:4]) # blank gives initial or final i.e [0:]
print(name[3:2]) #if given like this ntg is print with no error
print(name[-4:-1]) # numbering starts from the extreme right as -1 going left onwards -2,-3 and so on till the length

#skipping inbetween string
identification = "adityasantoshdhuri"
print(identification[0:16:2]) #here 0 indicate the start 16 indicate the no (i want) and 2 indicate gap between 0-16

