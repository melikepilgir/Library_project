class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn

        }
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"] , data ["author"] , data["isbn"])

import json

class Library:
    def __init__(self, filename= "library.json"):
        self.filename = filename
        self.books= []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r", encoding= "utf-8") as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            self.books = []
    def save_books(self):
        with open(self.filename, "w", encoding = "utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)


    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            print ("A book with this ISBN already exists.")
            return False
        self.books.append(book)
        self.save_books()
        print ("Book added successfully.")
        return True
    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                self.save_books()
                print ("Book removed successfully.")
                return True
        print ("Book is not found.")
        return False
    def list_books(self):
        if not self.books:
            print ("No books in the library.")
        else:
            for book in self.books:
                print(book)
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Find Book")
        print("5. Exit")

        choice = input("Enter your choice: (1-5): ").strip()
        if choice == "1":
            # Add Book
            while True:
                title = input("Book title: ").strip()
                if title:
                    break
                print("Title cannot be empty.")

            while True:
                author = input("Author: ").strip()
                if author:
                    break
                print("Author cannot be empty.")

            while True:
                isbn = input("ISBN: ").strip()
                if isbn and not any(b.isbn == isbn for b in library.books):
                    break
                elif not isbn:
                    print("ISBN cannot be empty")
                else:
                    print(" A book with this ISBN already exists. Please enter a different ISBN")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == "2":
            # Remove Book
            isbn = input("Enter ISBN of the book to remove: ").strip()
            library.remove_book(isbn)

        elif choice == "3":
            # List Books
            library.list_books()

        elif choice == "4":
            # Find Books
            isbn = input("Enter ISBN of the book to find: ").strip()
            book = library.find_book(isbn)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == "5":
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__=="__main__":
    main()
    # Second Stage is completed.











