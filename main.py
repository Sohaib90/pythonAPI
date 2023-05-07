from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the course of API development!"}

@app.get("/posts")
def get_posts():
    return {"posts": ["This is post 1", "This is post 2", "This is post 3"]}
