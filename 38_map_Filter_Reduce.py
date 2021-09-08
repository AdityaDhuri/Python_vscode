# Map

def square(num):
    return num*num
l = [2, 4, 5]

        # Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)    

       # Method 2
print(list(map(square, l)))

# Filter Function
def greter(num):
    if num > 5:
        return True
    else:
        return False

g = lambda num: num > 10
l = [1, 5, 10, 15]
print(list(filter(g, l)))
print(list(filter(greter, l)))

#Reduce
from functools import reduce

sum = lambda a, b: a+b
l = [1, 2, 3, 4]
val = reduce(sum, l)
print(val)