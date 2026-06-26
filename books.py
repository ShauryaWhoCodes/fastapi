from fastapi import FastAPI

app = FastAPI()


@app.get("/hello-world")
async def first_api():
    return {"message": "Hello World!!"}


Books = [
    {
        "id": 1,
        "title": "The Book",
        "author": "Joe Stantham",
        "subject": "History"},
    {
        "id": 2,
        "title": "The Alchemy Book",
        "author": "Danny Mathur",
        "subject": "Maths"},
    {
        "id": 3,
        "title": "Focus",
        "author": "Freddy",
        "subject": "Philosophy"
    },
    {
        "id": 4,
        "title": "deep work",
        "author": "Freddy",
        "subject": "science"
    }
]


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
