from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library_end import Library
from book import Book


app = FastAPI(title="Library API", description="Library API", version="1.0")

library = Library()

# Pydantic Methods
class ISBNRequest(BaseModel):
    isbn: str
class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str
# Endpoints

@app.get("books", response_model= list[BookResponse])
def get_books():
    return [book.to_dict() for book in library.books]

@app.post("/books", response_model=BookResponse)
def add_book(req: ISBNRequest):
    success= library.add_book(req.isbn)
    if not success:
        raise HTTPException(status_code=400, detail="Book is not added. ISBN is not valid.")

    book = library.find_book(req.isbn)
    return book.to_dict()
@app.delete("/books/{isbn}")
def delete_book(isbn: str):

    success = library.remove_book(isbn)
    if not success:
        raise HTTPException(status_code=404, detail="Book is not found.")
    return {"message": f" Book with ISBN {isbn} was deleted successfully." }


