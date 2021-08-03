# open a text file:

f = open('bocha.txt','r') # if r is not used it will show the same. it will consider r as by-default
data = f.read() # data is variable here
#data = f.read(5) this will give the first 5 characters/letters
#data = f.readline() this will only read the first line. if used  multiple times gives according lines
print(data)
f.close()

#create a text file using python:

f = open('bana.txt', 'w')
f.write("my name is bana\ni am ankita") #running the program again and again with different text will replace the text with the original text
f.close()

#update a exisiting file / appending

f = open('bana.txt', 'a') # running the program again and again will add the statemnts again and again at the end of senetence
f.write("i am bocha") #this will print on the same line the last statement was
f.close()
# if u erase or cut something from the text file always save the file

# openining text inside a file using with:
with open('bana.txt','r') as f:
    a = f.read() 
print(a)    

#rewriting a text inside a file using with: 
with open('bocha.txt','w') as f:
    a = f.write("i am ankita")
print(a)