from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float

    def __init__(self, id: int, title: str, author: str, description: str, rating: float):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None, description="Id is only needed when creating a new book")
    title: str = Field(min_length=4)
    author: str = Field(min_length=5)
    description: str = Field(min_length=2, max_length=100)
    rating: float = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book1",
                "author": "Author1",
                "description": "Description1",
                "rating": 2
            }
        }
    }

Books = [
    Book(1, 'Book1', author='Author1', description='Description1', rating=5.0),
    Book(2, 'Book2', author='Author2', description='Description2', rating=3.0),
    Book(3, 'Book3', author='Author3', description='Description3', rating=2.0),
    Book(4, 'Book4', author='Author4', description='Description4', rating=4.0),
    Book(5, 'Book5', author='Author5', description='Description5', rating=5.0),
]

@app.get("/read_all_books")
async def read_all_books():
    return Books

# fetch book using a id
@app.get("/read_book/{id}")
async def read_book(id: int):
    for book in Books:
        if book.id == id:
            return book

# fetch book using a id
@app.get("/read_book/")
async def read_book(rating: int):
    books = []
    for book in Books:
        if book.rating == rating:
            books.append(book)
    return books



#Create a new book
@app.post("/create-book")
async def create_new_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(assign_new_book_id(new_book))

def assign_new_book_id(book: Book):

    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book