from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def update_book_info(self, title=None, author=None, year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year

    def get_book_info(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
        }


app = FastAPI()

books = dict()


class BookSchema(BaseModel):
    title: str
    author: str
    year: int


@app.get("/books")
def get_books():
    return books


@app.get("/books/{isbn}")
def get_book(isbn: str):
    for key, value in books.items():
        if key == isbn:
            return {
                "isbn": isbn,
                "title": value[0],
                "author": value[1],
                "year": value[2]
                }
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def add_book(isbn: str, book: BookSchema):
    if isbn in books:
        raise HTTPException(status_code=400, detail="ISBN already exists")
    try:
        books[isbn] = [book.title, book.author, book.year]
        return {"message": "Book added successfully"}
    except Exception as e:
        return e


@app.put("/books/{isbn}")
def update_book(isbn: str, book: BookSchema):
    if isbn in books:
        books[isbn] = [book.title, book.author, book.year]
        return {"message": "Book updated"}
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if isbn in books:
        del books[isbn]
        return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
