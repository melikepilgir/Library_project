import json
from book import Book
import httpx


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