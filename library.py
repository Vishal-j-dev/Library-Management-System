from datetime import datetime
class Book:
    def __init__(self,title):
        self.title=title
        self.datetime=datetime.now()
        self.__available=True
    def is_available(self):
        return self.__available
    
    def issue(self):
        if self.__available:
            self.__available=False
            print("Book issued")
        else:
            print("not available")

    def return_book(self):
        self.__available=True
        print("Book Returned")
class User:
    def __init__(self,name):
        self.name=name
        self.borrowed={}
    
    def user_book(self):

        for title,records in self.borrowed.items():
            print(f"\n{title}:")
            for r in records:
                print(f"Issued : {r['issued_at']} | Returned:{r['returned']}")
class Library:
    def __init__(self):
        self.__books={"python":2,"c":3}
    
    def add(self,title):
        title=title.lower()
        if title in self.__books:
            self.__books[title]+=1
        else:
            self.__books[title]=1

        print("Successfully added")

    def show(self):
        print("\nAvailable Books")
        print(self.__books)

    def issue(self,title,user):
        title=title.lower()
        if title in self.__books and self.__books[title]>0:
            self.__books[title]-=1
            
            now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if title not in user.borrowed:
                user.borrowed[title]=[]

            user.borrowed[title].append({"issued_at":now,"returned_at":None})
            print(f"Book issued at {now}")

        else:
        
            print("book is not available")

    def return_book(self,title,user):
        title=title.lower()
        if title in user.borrowed:
            now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for i in reversed(user.borrowed[title]):
                if i["returned_at"] is None:
                    i["returned_at"]=now
                    self.__books[title]+=1
                    print(f"book returned at {now}")
                    return
            print("All copies returned")
        else:
            print("You dont have this book")
    def search(self,title):
        title=title.lower()
        if title in self.__books:
            print(f"found:{title}-{self.__books[title]}")
        else:
            print("Book not found")


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
    def add_books(self,library,title):
        library.add(title)
        print("Book was added")
class Authentication:
    def __init__(self):
        self.__user={}
    
    def register(self):
        name=input("Enter Your Name:").lower()
        if name in self.__user:
            print("user already exists")
            return
        
        password=input("enter password: ")
        role = input("Enter role (admin/user): ").lower()
        if role == "admin":
            user_obj=Admin(name)
        else:
            user_obj=User(name)
        self.__user[name] = {
        "user": user_obj,
        "password": password
    }

        print(f"{role} registered successfully!")
    def login(self):
        name=input("Enter Your Name: ").lower()
        if name in self.__user:
            password=input("Enter Password: ")
            if password == self.__user[name]["password"]:
                print("Login success")
                return self.__user[name]["user"]
            else:
                print("Wrong password")
                return None

        else:
            print("User Does'nt exist")

def main():
    lib=Library()
    auth=Authentication()
    while True:
        print("\n 1.Register")
        print("2.Login")
        print("3.Exit")

        choice=input("Enter Your Choice: " )

        match choice:
            case "1":
                auth.register()
        
            case "2":
                user=auth.login()
                if user:
                    user_menu(lib,user)

            case "3":
                print("Thank you")
                break
def user_menu(lib,user):
 
    while True:
        print("\nLIBRARY MENU")
        print("1.Add Book")
        print("2.Show Book")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Search Book")
        print("6.User books")
        print("7.Exit")

        choice=input("Enter Your Choice: ")

        match choice:
            case "1":
                title = input("Enter book title: ")

                if isinstance(user, Admin):
                    user.add_books(lib, title)
                else:
                    print("Only admin can add books!")
            case "2":
                lib.show()
            case "3":
                title=input("Enter Title : ").strip().lower()
                lib.issue(title,user)
            case "4":
                title=input("Enter Title : ")
                lib.return_book(title,user)
            case "5":
                title=input("Enter Title : ")
                lib.search(title)
            case "6":
                user.user_book()
            case "7":
                print("Thank You")
                break

if __name__=="__main__":
    main()

