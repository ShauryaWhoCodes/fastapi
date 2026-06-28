from fastapi import FastAPI, Body

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


Books = [
    Book(1, 'Book1', author='Author1', description='Description1', rating=5.0),
    Book(2, 'Book2', author='Author2', description='Description2', rating=3.0),
    Book(3, 'Book3', author='Author3', description='Description3', rating=2.0),
    Book(4, 'Book4', author='Author4', description='Description4', rating=4.0),
    Book(5, 'Book5', author='Author5', description='Description5', rating=1.0),
]

@app.get("/read_all_books")
async def read_all_books():
    return Books

#Create a new book
@app.post("/create-book")
async def create_new_book(new_book=Body()):
    Books.append(new_book)