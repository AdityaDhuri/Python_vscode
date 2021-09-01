a = 50 #Gobal Variable
def function():
    global a
    a = 8    # Local Variable

    print(a)
function() 
print(a)   