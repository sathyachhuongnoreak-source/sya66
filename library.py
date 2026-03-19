class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f'Title: {self.title} -- Author: {self.author} -- ISBN: {self.isbn} [{status}]'

class Member:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.books_borrowed = []

    def __str__(self):
        return f'Name: {self.name} -- Age: {self.age} -- Books: {len(self.books_borrowed)}'

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully!")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return 

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return 

    def borrow_book(self, member_name, isbn):
        member = self.find_member(member_name)
        book = self.find_book(isbn)

        if member and book:
            if not book.is_borrowed:
                book.is_borrowed = True
                member.books_borrowed.append(book)
                print(f"{member.name} successfully borrowed '{book.title}'")
            else:
                print("Sorry, this book is already borrowed.")
        else:
            print("Member or Book not found.")

    def return_book(self, member_name, isbn):
        member = self.find_member(member_name)
        book = self.find_book(isbn)

        if member and book in member.books_borrowed:
            book.is_borrowed = False
            member.books_borrowed.remove(book)
            print(f"{member.name} successfully returned '{book.title}'")
        else:
            print("Return failed. Check member name or ISBN.")

library = Library()

while True:
    print('''
========== Library System ==========
1. ADD BOOK
2. ADD MEMBER
3. FIND BOOK
4. FIND MEMBER
5. BORROW BOOK
6. RETURN BOOK
0. EXIT
====================================
    ''')
    choice = input("Input choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author Name: ")
        isbn = input("ISBN Code: ")
        library.add_book(Book(title, author, isbn))

    elif choice == "2":
        name = input("Member Name: ")
        gender = input("Gender: ")
        age = input("Age: ")
        library.add_member(Member(name, gender, age))

    elif choice == "3":
        isbn = input("Enter ISBN to find: ")
        book = library.find_book(isbn)
        print(book if book else "Book not found.")

    elif choice == "4":
        name = input("Enter Member Name to find: ")
        mem = library.find_member(name)
        print(mem if mem else "Member not found.")

    elif choice == "5":
        m_name = input("Member Name: ")
        isbn = input("Book ISBN: ")
        library.borrow_book(m_name, isbn)

    elif choice == "6":
        m_name = input("Member Name: ")
        isbn = input("Book ISBN: ")
        library.return_book(m_name, isbn)
    
    elif choice == "0":
        print("Bye bye")
        break