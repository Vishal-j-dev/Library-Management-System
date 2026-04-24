from datetime import datetime
import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vishal@12",
    database="library"
)
cursor = conn.cursor()


# ---------------- USER CLASS ----------------
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def user_book(self):
        cursor.execute("""
            SELECT b.title, t.issued_at, t.returned_at
            FROM transactions t
            JOIN books b ON t.book_id = b.book_id
            WHERE t.user_id = %s
        """, (self.user_id,))

        records = cursor.fetchall()

        if not records:
            print("No books borrowed")
            return

        for r in records:
            print(f"{r} \n Issued: {r[1]} | Returned: {r[2]}")
    def view_user(self):
        cursor.execute("""select * from Users""")

        result=cursor.fetchall()
        for i in result:
            print(i,"\n")

# ---------------- ADMIN CLASS ----------------
class Admin(User):
    def add_books(self,library, title):
        library.add(self.user_id,title)
        print("Book was added")
    def delete_books(self,library,title):
        library.delete(self.user_id,title)
        print("book was deleted")
    def view_userbooks(self):
        cursor.execute("""select u.user_id,u.name,b.title,b.book_id,t.issued_at,t.returned_at
                       from transactions t join users u on t.user_id=u.user_id
                       join books b on t.book_id=b.book_id""")
        result=cursor.fetchall()
        for i in result:
            print(i,"\n")


# ---------------- LIBRARY CLASS ----------------
class Library:

    def add(self, user_id, title):
        title = title.lower()

        # Check role
        cursor.execute("SELECT role FROM users WHERE user_id=%s", (user_id,))
        result = cursor.fetchone()

        if not result:
            print("Invalid user_id")
            return

        role = result[0]

        if role.strip().lower() != "admin":
            print("Only admin can add books")
            return

        # 🔥 Get latest book (avoids unread result error)
        cursor.execute("""
            SELECT book_id, status 
            FROM books 
            WHERE title=%s 
            ORDER BY book_id DESC 
            LIMIT 1
            """, (title,))
    
        new = cursor.fetchone()

        if new:
            book_id, status = new

            if status != -1:
            # ✅ Book exists → increase count
                cursor.execute("""
                    UPDATE inventory 
                    SET total_copies = total_copies + 1,
                    available_copies = available_copies + 1
                    WHERE book_id=%s
                """, (book_id,))
            else:
            # ✅ Book was deleted → create NEW entry
                cursor.execute("INSERT INTO books (title) VALUES (%s)", (title,))
                book_id = cursor.lastrowid

                cursor.execute("""
                    INSERT INTO inventory (book_id, total_copies, available_copies)
                    VALUES (%s, 1, 1)
                """, (book_id,))
        else:
        # ✅ Completely new book
            cursor.execute("INSERT INTO books (title) VALUES (%s)", (title,))
            book_id = cursor.lastrowid

            cursor.execute("""
                INSERT INTO inventory (book_id, total_copies, available_copies)
                VALUES (%s, 1, 1)
            """, (book_id,))

        conn.commit()
        print("Successfully added")
    def delete(self,user_id,title):
        title = title.lower()

        cursor.execute("SELECT role FROM users WHERE user_id=%s", (user_id,))
        result = cursor.fetchone()

       

        if not result:
            print("Invalid user_id")
            return
        
        role= result[0]
       
        if role and role.lower()=="admin":
            cursor.execute("""select book_id from books where title=%s""",(title,))
            new=cursor.fetchone()
            if new:
                book_id=new[0]
                cursor.execute("""
                    UPDATE inventory 
                    SET total_copies = 0,
                    available_copies = 0
                    WHERE book_id=%s
                    """, (book_id,))
                cursor.execute("""update books set status=-1,deleted_at=current_timestamp where title=%s""",(title,))
                conn.commit()
                print("deleted a book")
            else:
                print("Entered book is not there")
        else:
            print("only admin can delete books")

    def show(self):
        cursor.execute("""
            SELECT b.title, i.available_copies
            FROM books b
            JOIN inventory i ON b.book_id = i.book_id
        """)

        books = cursor.fetchall()

        print("\nAvailable Books:")
        for b in books:
            print(f"{b[0]} : {b[1]}")

    def issue(self, title, user):
        title = title.lower()

        cursor.execute("""
            SELECT b.book_id,b.status, i.available_copies
            FROM books b
            JOIN inventory i ON b.book_id = i.book_id
            WHERE b.title=%s
        """, (title,))

        result = cursor.fetchone()

        if result and result[1] != -1:
            book_id = result[0]

            cursor.execute("""
                INSERT INTO transactions (user_id, book_id, issued_at)
                VALUES (%s, %s, NOW())
            """, (user.user_id, book_id))

            cursor.execute("""
                UPDATE inventory
                SET available_copies = available_copies - 1
                WHERE book_id=%s
            """, (book_id,))

            conn.commit()
            print("Book issued")
        

        else:
            print("Book not available")

    def return_book(self, title, user):
        title = title.lower()

        cursor.execute("""
            SELECT t.transaction_id, b.book_id
            FROM transactions t
            JOIN books b ON t.book_id = b.book_id
            WHERE b.title=%s AND t.user_id=%s AND t.returned_at IS NULL
            ORDER BY t.issued_at DESC LIMIT 1
        """, (title, user.user_id))

        result = cursor.fetchone()

        if result:
            transaction_id, book_id = result

            cursor.execute("""
                UPDATE transactions 
                SET returned_at = NOW()
                WHERE transaction_id=%s
            """, (transaction_id,))

            cursor.execute("""
                UPDATE inventory
                SET available_copies = available_copies + 1
                WHERE book_id=%s
            """, (book_id,))

            conn.commit()
            print("Book returned")

        else:
            print("No record found")

    def search(self, title):
        title = title.lower()

        cursor.execute("""
            SELECT b.title, i.available_copies
            FROM books b
            JOIN inventory i ON b.book_id = i.book_id
            WHERE b.title=%s
        """, (title,))

        result = cursor.fetchone()

        if result:
            print(f"{result[0]} - Available: {result[1]}")
        else:
            print("Book not found")


# ---------------- AUTHENTICATION ----------------
class Authentication:

    def register(self):
        name = input("Enter Your Name: ").lower()
        password = input("Enter password: ")
        role = input("Enter role (admin/user): ").strip().capitalize()

        cursor.execute("SELECT user_id,role,status FROM users WHERE name=%s and password=%s", (name, password))
        result=cursor.fetchone()
        if result:
            user_id,role,status=result
            status=result[2]
            if status==1:
                print("User already exists")
                return
            elif status==0:
                print("registered already go to login")
                return
            else:
                print("user was deleted")
                return
            
    
        cursor.execute("""
            INSERT INTO users (name, password, role)
            VALUES (%s, %s, %s)
            """, (name, password, role))

        conn.commit()
        print(f"{role} registered successfully!")

    def login(self):
        name = input("Enter Your Name: ").lower()
        password = input("Enter Password: ")

        cursor.execute("""
            SELECT user_id, role,status FROM users
            WHERE name=%s AND password=%s
        """, (name, password))

        result = cursor.fetchone()

        if result:
            user_id, role ,status= result
            status=result[2]
            if status==0:
                cursor.execute("""update users set status=1 where user_id=%s""",(user_id,))
                print("Status updated , login succeed")
            elif status==1:
                print("Login success")
                if role.strip().lower() == "admin":
                    return Admin(name, user_id)
                else:
                    return User(name, user_id)
            elif status==-1:
                print("you deleted your account")

           
        else:
            print("Invalid credentials")
            return None
    def logout(self):
        name=input("Enter your name: ").lower()
        password=input("Enter Password: ")

        cursor.execute("""Select user_id,role,status from users where name =%s and password=%s""",(name,password))
        result=cursor.fetchone()

        if result:
            user_id,role,status=result
            status=result[2]
            if status==1:
                cursor.execute("""update users set status=0 where user_id=%s""",(user_id,))
                conn.commit()
                print("logged out successfully")
            elif status==0:
                print("your account has been logged out login first")
            else:
                print("Your account doesn't exist")
        else:
            print("Invalid credentials")

    def delete(self):
        name=input("Enter Your Name: ").lower()
        password=input("Enter Password: ")
        cursor.execute("""select user_id,role,status from users where name=%s and password=%s""",(name,password))
        result=cursor.fetchone()

        if result:
            user_id,role,status=result
            status=result[2]
            if status==1 or status==0:
                cursor.execute("""update users set status=-1, deleted_at=current_timestamp where user_id=%s""",(user_id,))
                conn.commit()
                print("Deleted successfully")
            elif status==-1:
                print("Account doesn't exist ")

# ---------------- MAIN ----------------
def main():
    lib = Library()
    auth = Authentication()

    while True:
        print("\n1.Register")
        print("2.Login")
        print("3.Logout")
        print("4.delete")
        print("5.exit")

        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                auth.register()

            case "2":
                user = auth.login()
                if isinstance(user, Admin):
                    admin_menu(lib, user)
                else:
                    user_menu(lib, user)

            case "3":
                auth.logout()
            case "4":
                user=auth.delete()
                if isinstance(user,Admin):
                    admin_menu(lib,user)
                else:
                    user_menu(lib,user)
            case "5":
                print("Thank You")
                break;
                    


# ---------------- USER MENU ----------------
def user_menu(lib, user):
    while True:
        print("\nLIBRARY MENU")
       
        print("1.Issue Book")
        print("2.Return Book")
        print("3.Search Book")
        print("4.User books")
        print("5.delete account")
        print("6.Exit")

        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                title = input("Enter Title: ")
                lib.issue(title, user)
                
            case "2":
                title = input("Enter Title: ")
                lib.return_book(title, user)

            case "3":
                title = input("Enter Title: ")
                lib.search(title)
                

            case "4":
               user.user_book()

            case "5":
                lib.delete()

            case "6":
                print("Thank You Visit Again")
                break

def admin_menu(lib,user):
    while True:
        print("\n Admin Menu")
        print("1.Add Book")
        print("2.delete book")
        print("3.Show Book")
        print("4.view users")
        print("5.User books")
        print("6.delete account")
        print("7.exit")
        choice=input("enter your choice admin: ")
        match choice:
            case "1":
                title = input("Enter book title: ")

                if isinstance(user, Admin):
                    user.add_books(lib, title)
                else:
                    print("Only admin can add books!")
            case "2":
                title = input("Enter book title: ")

                if isinstance(user, Admin):
                    user.delete_books(lib, title)
                else:
                    print("Only admin can delete books!")
            case "3":
                lib.show()
            case "4":
                user.view_user()
            case "5":
                user.view_userbooks()
            case "6":
                lib.delete()
            case "7":
                print("Done")
                break

            
            


if __name__ == "__main__":
    main()
