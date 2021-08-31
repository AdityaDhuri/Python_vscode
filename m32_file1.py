#using function from one file to another
def greet(name):
    print(f"Good Morning, {name}")

if __name__ == "__main__":
    n = input("Enter a name: ")
    greet(n)