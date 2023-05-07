from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
################################################################
# Define how data should be in pure, canonical Python; validate it with pydantic.
from pydantic import BaseModel # create a schema for the post request
################################################################


app = FastAPI()

# pydantic BaseModel extension for custom schema validation
class Post(BaseModel):
    title: str
    content: str
    pusblish: bool = True
    # add an optional property
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the course of API development!"}

@app.get("/posts")
def get_posts():
    return {"posts": ["This is post 1", "This is post 2", "This is post 3"]}

# post request: usually sent by the end user to the server to store data
# return in the function is to indicate whether the request was successful
@app.post("/createposts")
def create_post(post : Post):
    # FastAPI handles the checking of the schema itself when we pass Post(BaseModel) type object
    return post.dict()
