from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from datetime import date, datetime

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    published_date: date

    def __init__(self, id: int, title: str, author: str, description: str, rating: float, published_date: date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None, description="Id is only needed when creating a new book")
    title: str = Field(min_length=4)
    author: str = Field(min_length=5)
    description: str = Field(min_length=2, max_length=100)
    rating: float = Field(gt=0, lt=6)
    published_date: date = Field(ge=date(2000, 1, 1), lt=date.today())

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book1",
                "author": "Author1",
                "description": "Description1",
                "rating": 2,
                "published_date": date(2000, 1, 1),
            }
        }
    }

Books = [
    Book(1, 'Book1', author='Author1', description='Description1', rating=5.0, published_date=date(2000, 1, 1)),
    Book(2, 'Book2', author='Author2', description='Description2', rating=3.0, published_date=date(2002, 12, 2)),
    Book(3, 'Book3', author='Author3', description='Description3', rating=2.0, published_date=date(2003, 2, 3)),
    Book(4, 'Book4', author='Author4', description='Description4', rating=4.0, published_date=date(2004, 2, 2)),
    Book(5, 'Book5', author='Author5', description='Description5', rating=5.0, published_date=date(2005, 10, 12)),
]

@app.get("/read_all_books")
async def read_all_books():
    return Books

# fetch book using an id
@app.get("/book/{id}")
async def read_book(id: int = Path(gt=0)):
    for book in Books:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Fetch book using published date
@app.get("/books/{published_date}")
async def read_books(published_date: str):
    published_date = datetime.strptime(published_date, "%Y-%m-%d").date()
    for book in Books:
        if book.published_date == published_date:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# fetch book using the rating
@app.get("/book/")
async def read_book(rating: int = Query(gt=0, lt=6)):
    books = []
    for book in Books:
        if book.rating == rating:
            books.append(book)
    if len(books) == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return books

# update the book using ID
@app.put("/update_book/")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = book
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")
# Delete a book using id
@app.delete("/book/{id}")
async def delete_book(id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(Books)):
        if Books[i].id == id:
            Books.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Book not found")

#Create a new book
@app.post("/create-book")
async def create_new_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(assign_new_book_id(new_book))

def assign_new_book_id(book: Book):

    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book