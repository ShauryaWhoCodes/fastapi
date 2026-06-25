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
    }
]


@app.get("/books")
async def get_books():
    return Books
