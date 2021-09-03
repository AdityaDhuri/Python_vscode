a = [3, 4, 5, 6, 8, 10, 11, 3, 10, 6]
#b=[]
#for item in a:
#    if item%2==0:
#        b.append(item)
#print(b)        
b = [i for i in a if i%2==0] #shortcut to write the same
print(b)   #it will print all the values if repeated also
c = {i for i in a if i>6}
print(c)   #it will print all the values if repeated also
d = {i for i in a} #set wont allow repeated values