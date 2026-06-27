from fastapi import Body, FastAPI
from common import Books

app = FastAPI()

@app.get("/hello-world")
async def first_api():
    return {"message": "Hello World!!"}

@app.get("/books")
async def get_books():
    return Books


# find book by its title
@app.get("/books/{title}")
async def get_books_using_title(title: str):
    for book in Books:
        if book.get("title").casefold() == title.casefold():
            return book
    return {"message": "No book found"}

# Query parameter
@app.get("/books/{author}/")
async def get_books_using_author(author: str, subject: str):
    books = []
    for book in Books:
        if book.get("author").casefold() == author.casefold() and book.get("subject") == subject.casefold():
            books.append(book)
    return books

# Create a new book
@app.post("/books/new_book")
async def create_new_book(new_book=Body()):
    Books.append(new_book)

