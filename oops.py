""""class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def show(self):
        print(self.brand,self.price)
c1=Car("BMW",500000)
c1.show()"""
"""
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def show(self):
        print("balance",self.__balance)

a=BankAccount(1000)
a.deposit(500)
a.withdraw(200)
a.show()"""
"""class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def discount(self,price):
        self.price-=price
    
    def show(self):
        print(self.brand,self.price)

c1=Car("BMW",100000)
c2=Car("Audi",100022)
c1.discount(5000)
c1.show()
c2.show()
"""
"""class Vishal:
    x=5
a=Vishal()
print(a.x)"""

"""class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        self.total=self.length*self.width
        print("area : ",self.total)
a=Rectangle(20,30)
a.area()
"""
"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def total(self):
        total=0
        for i in self.marks:
            total+=i
        return total
        
    def average(self):
        total=self.total()
        return total/len(self.marks)
       
    
s1=Student("surya",[30,40,50,90])
s2=Student("Vishal",[50,50,80,90])
print(s1.total())
print(s2.total())
print(s1.average())
print(s2.average())
"""

class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
c1=car("BMW",200)
c2=car("skoda",300)

class Mobile:
    def __init__(self,brand,battery):
        self.brand=brand
        self.battery=battery
    def both(self):
        print(f"{self.brand},{self.battery}")

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def add(self):
        sum=0
        for i in self.marks:
            sum+=i
        return sum
    def average(self):
        count=0
        for i in self.marks:
            count+=1
        return count
    def result(self):
        return self.add()/self.average()
    def highest(self):
        a=0
        for i in range(len(self.marks)):
            if self.marks[i]>a:
                a=self.marks[i]
        return a
s1=Student("vishal",[20,30,40,100])

"""
class Book:
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id
        self.available=True
        
    def borrow(self):
        if self.available:
            self.available=False
            print("book borrowed")
        else:
            print("Book not available")
    
    def return_book(self):
        self.available=True
        print("Book returned")
class User:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.track_borrow=[]
    def borrow(self,book):
        self.track_borrow.append(book)
    def return_book(self,book):
        self.track_borrow.remove(book)
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def issue_book(self, user, book):
        if book.available:
            book.borrow()
            user.borrow(book)
        else:
            print("Book not available")

    def return_book(self, user, book):
        book.return_book()
        user.return_book(book)


lib = Library()

b1 = Book("Python", "Guido", 101)
u1 = User("Vishal", 1)

lib.add_book(b1)
lib.add_user(u1)

lib.issue_book(u1, b1)
lib.return_book(u1, b1)
"""
        
from datetime import datetime

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__available=True
        self.datetime=datetime.now()
    
    def is_available(self):
        return self.__available
    
    def issue(self):
        self.__available=False
    
    def return_book(self):
        self.__available=True

class User:
    def __init__(self,name):
        self.name=name
        self.borrowed_books={}
        self.date={}

    def show_user_books(self):
        print("\nYour Books:")
        print(self.borrowed_books)
        for title, records in self.borrowed_books.items():
            print(f"\n{title}:")
            for r in records:
                print(f"  Issued: {r['issued_at']} | Returned: {r['returned_at']}")
    
class Library:
    def __init__(self):
        self.__books={"python":5,"c":2,"java":3}
    def add_book(self,title):
        title=title.lower()
        if title in self.__books:
            self.__books[title]+=1
        else:
            self.__books[title]=1
    def show_books(self):
        print("\n Availabel Books: ")
        for title,count in self.__books.items():
            print(f"{title.title()}-{count}")
    def issue_book(self,title,user):
        title=title.lower()
        if title in self.__books and self.__books[title]>0:
            self.__books[title]-=1

            now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if title not in user.borrowed_books:
                user.borrowed_books[title]=[]
            
            user.borrowed_books[title].append({
                "issued_at":now,
                "returned_at":None
            })
            print(f"Book issued at {now}")
        else:
            print("Book is not available")
    def return_book(self, title, user):
        title=title.lower()
        if title in user.borrowed_books and user.borrowed_books[title]:
            now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for i in reversed(user.borrowed_books[title]):
                if i["returned_at"] is None:
                    i["returned_at"]=now
                    break
            self.__books[title]+=1
            
            print(f"Book returned at {now}")
        else:
            
            print("This user doesn't have this book")
    def search_book(self, title):
        title=title.lower()
        if title in self.__books:
            print("Found:",title, "-", self.__books[title])
            return
        print("Book not found")
class Admin(User):
    def __init__(self,name):
        super().__init__(name)
    def add_book_to_library(self, library, book):
        library.add_book(book)
        print("Admin added book")
class Authsystem:
    def __init__(self):
        self.__users={}
    def register(self):
        name=input("Enter Username : ").lower()

        if name in self.__users:
            print("User already exists")
            return
        password=input("enter password:")

        self.__users[name]={
            "user":User(name),
            "password":password
        }   

        print("USer registered")

    def login(self):
        name = input("Enter username: ").lower()
        password = input("Enter password: ")
    
        if name in self.__users and self.__users[name]["password"] == password:
            print("Login successful!")
            return self.__users[name]["user"]
        else:
            print("Invalid credentials!")
            return None

def main():
    lib = Library()
    admin = Admin("Admin")
    auth = Authsystem()

    

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            auth.register()

        elif choice == "2":
            user = auth.login()

            if user:
         
                user_menu(lib, user, admin)

        elif choice == "3":
            break
def user_menu(lib,user,admin):
    while True:
        print("\nLIBRARY MENU")
        print("1.Add Book")
        print("2.Show Book")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Search Book")
        print("6.User books")
        print("7.Exit")

        choice=input("Enter choice:")
        match choice:
            case "1":
                title = input("Enter book title: ")
                admin.add_book_to_library(lib, title)

            case "2":
                lib.show_books()

            case "3":
                title = input("Enter book title to issue: ")
                lib.issue_book(title,user)

            case "4":
                title = input("Enter book title to return: ")
                lib.return_book(title,user)

            case "5":
                title = input("Enter book title to search: ")
                lib.search_book(title)

            case "6":
                user.show_user_books()

            case "7":
                print("Exiting system...")
                break

            case _:
                print("Invalid choice! Try again")


if __name__ == "__main__":
    main()