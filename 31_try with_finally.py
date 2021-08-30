try:
    i = int(input("enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:       
    print("We are done")  #this is something that will execute even if you use exit()