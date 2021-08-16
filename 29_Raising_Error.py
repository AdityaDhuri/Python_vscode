
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is bad-------by Aditya")    

a = increment('4nk')
print(a)        