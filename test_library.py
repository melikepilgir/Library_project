import os
import pytest
from book import Book
from library_end import Library

TEST_FILE = "test_library.json"

@pytest.fixture
def lib():

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_and_find_book(lib):
    book = Book("Test Title", "Test Author", "123456")
    lib.books.append(book)
    lib.save_books()

    found = lib.find_book("123456")
    assert found is not None
    assert found.title == "Test Title"
def test_remove_book(lib):
    book = Book("ToRemove", "Author", "654321")
    lib.books.append(book)
    lib.save_books()

    result = lib.remove_book("654321")
    assert result is True
    assert lib.find_book("654321") is None
def test_list_books_empty(lib, capsys):
    lib.books = []
    lib.save_books()
    lib.list_books()
    captured = capsys.readouterr()
    assert "No books found" in captured.out

