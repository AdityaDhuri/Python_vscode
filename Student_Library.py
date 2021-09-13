# Implement a STUDENT LIBRARY system using OOP where students can borrow a book from the list of books. Create a seperste library and student class. Your program must be menu driven.

class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in the Library are: ")
        for book in self.books:
            self.books.sort()
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please return within 30days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry the book is either not available or has already issued to someone else. Please wait until the book is available")        
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        self.books.sort()
        print("Thanks for Adding/returning the book!")



class Student:
    
    def requestBook(self):
        self.book  = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to Add/Return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes", "Chacha Chaudhary", "Folk Tales"])
    #centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        welcomemsg = '''
        ===== Welcome to Central Library =====
        Please choose an option:
        1. List of all Books Available
        2. Request a Book
        3. Add/Return a Book
        4. Exit the Library
        '''
        print(welcomemsg)
        try :
            a = input("Enter a Choice: ")
            a = int(a)
            if a == 1:
                centralLibrary.displayAvailableBooks()
            elif a ==2:
                centralLibrary.borrowBook(student.requestBook())
            elif a == 3:
                centralLibrary.returnBook(student.returnBook())
            elif a == 4:
                print("Thanks for choosing Central Library!!")
                exit()       
            else:
                print("You have entered wrong option. Please Try Again!!")
        except Exception as e:
            print("You have entered wrong option. Please try again")