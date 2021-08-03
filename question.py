#Write a program to read the text from a given file 'poems.txt' and find out whether it contain the word 'twinkle'
'''
with open('poems.txt','r') as f:
    a = f.read()
print(a)
if 'twinkle' in a:
    print("twinkle is present")
else:
    print("twinkle is not present")

#The game() function in a program lets a user play a game and return the score as an integer. You need to read a file 'Hi_score.txt'which is either blank or contains previous Hi-score
#Write a program to update the hi-score whenever game() breaks the Hi-score

b = int(input("Enter your Hi_score: "))
def game():
    return b
score = game()

with open("Hi_score.txt") as f:
    Hi_score = f.read()
if (Hi_score == ''):
    with open("Hi_score.txt","w") as f:
        f.write(str(score))
elif int(Hi_score) < score :
    with open("Hi_score.txt","w") as f:
        f.write(str(score))

#Write a progrwm to generate  multiplication table from 2-20 an save it in different file:

for a in range(2,21):
    with open(f"tables/Multiplication_table_of_{a}.txt", 'w') as f:
        for i in range(1,11):
            f.write(f"{a} X {i} = {a*i}")
            if i!=10:
                f.write('\n')

# A file conatins a word "Donkey" multiple time. You need to write a progrwm to replace the word with ###### by updating the same file
with open("bocha.txt") as f:
    content = f.read()

content = content.replace("donkey","######")

with open('bocha.txt','w') as f:
    f.write(content)
 
# for above program. if list of words are given:
words = ["donkey", "monkey", "gandu"]
with open("bocha.txt") as f:
    content = f.read().lower() #adding .lower() at the end helps to find every possible value for the word eg. AdiTya/adiTYA etc everything will be detected as aditya but everything will be saved in lower case in content
for word in words:
    content = content.replace(word,"######")
    with open('bocha.txt','w') as f:
        f.write(content)
  
# write a program to mine a log file(i used normal file) and find whether it contains python   
with open('bocha.txt') as f:
    content = f.read()

if 'python' in content.lower(): #adding .lower() here will check every possibility and will not chanege in actual content when print
    print("yes it is present")
else:
    print("no not present")
        
# write a program to mine a log file(i used normal file) and find whether it contains python also find the line no:
content = True
i = 1
with open('bocha.txt') as f:
    while content:
        content = f.readline() #reads line 

        if 'python' in content.lower():
            print(content)
            print("yes python is present")
            print(i)
        i+=1        

# Write a program to make a copy of a text file:
with open('bocha.txt') as f:
    content = f.read()

with open('aditya.txt','w') as f:
    f.write(content)

# write a program to find whether  afile is identical and matches the content of another file:
with open('bocha.txt') as f:
    content = f.read()

with open('aditya.txt') as f:
    content2 = f.read()

if content == content2:
    print("they are identical")
else:
    print("they are not identical")    

#Write a program to wipe out the content inside a file using python:
with open('aditya.txt','w') as f:
    f.write("")

# Write a program to rename a file to rename_by_python.txt: (to delete previous file)
import os   #a function used here to remove 

oldname = "sample.txt"
newname = "rename_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname,'w') as f:
    f.write(content)

os.remove(oldname)    
'''