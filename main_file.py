from library_end import Library
from book import Book


def main():
    library = Library("library.json")

    while True:
        from library_end import Library


        print("=== Library Application ===")
        print("1. Add Book with ISBN")
        print("2. Remove Book with ISBN")
        print("3. List Books")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            isbn= input("Enter ISBN of the book: ")
            library.add_book(isbn)

        elif choice == "2":
            isbn = input("Enter ISBN of the book that you want to remove: ")
            library.remove_book(isbn)
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            isbn = input("Enter ISBN of the book that you want to find: ")
            book = library.find_book(isbn)
            if book:
                print(book)
            else:
                print("Book not found")
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()