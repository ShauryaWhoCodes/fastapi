from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
async def first_api():
    return {"message": "Hello World!!"}