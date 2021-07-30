# Write a program to print content of a list using for loop
'''
fruits = ['mango', 'banana', 'watermelon', 'grapes']
for item in fruits:
    print(item)

#range function
for i in range(0, 10, 2): #(start, end, gap)
    print(i)    
else:
    print("done")    

#break function
for i in range(10):
    print(i)    
    if i==5:
        break   # terminates/ends the loop if conditions meet
'''
#continue
for i in range(10):   
    if i==5:
        continue
    print(i) 
    
#pass statement
i = 0
if i<5:
    pass
print("using pass will not execute it therefore no error is shown but your above statement needs to be correct")