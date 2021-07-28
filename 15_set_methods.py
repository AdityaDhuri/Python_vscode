
a = set()
print(a)

#Adding values to an empty set
a.add(4)
a.add(4)
a.add(5)
a.add(7)
a.add((5, 8, 89)) #can add tuple boz they cannot be changed
print(a) # a set does not print repeated values

#Operations
print(len(a)) #prints length of a
a.remove(5)
print(a) #removes 5 from a
print(a.pop()) #removes random value from set
#a.clear()
#print(a) clears the set

#combining two sets or union of set and intersection of set
a = {4, 5, 8, 11}
b = {7, 8, 9, 4, 18}
c = b.union(a) #union or c = a.union(b) or c = b.union(a,b) or c = a.union(a,b) all will have same value
#c = a.union({7,9}) when u want to add new values directly. you have to create a new character
print(c)
d = a.intersection(a,b) #intersection
print(d)