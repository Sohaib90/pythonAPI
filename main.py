from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
import uuid
################################################################
# Define how data should be in pure, canonical Python; validate it with pydantic.
from pydantic import BaseModel # create a schema for the post request
################################################################
# Documentation for the API: http://127.0.0.1:8000/docs
# CRUD (Create, Read, Update and Delete)


app = FastAPI()

my_posts = []

# pydantic BaseModel extension for custom schema validation
class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    # add an optional property
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the course of API development!"}

@app.get("/posts")
def get_posts():
    return {"posts": my_posts}

# Get post by id
@app.get("/posts/{id}")
def get_post(id: str, response: Response):
     # find the post with the id
    for post in my_posts:
        if post["id"] == id:
            return {"post": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Post not found for the id: 664a829")

# post request: usually sent by the end user to the server to store data
# return in the function is to indicate whether the request was successful
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post : Post):
    # FastAPI handles the checking of the schema itself when we pass Post(BaseModel) type object
    post_dict = post.dict()
    # create a random unique id everytime I come here
    post_dict["id"] = str(uuid.uuid4())[:8]
    my_posts.append(post_dict)
    return {"data": my_posts}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
     # delete post by id
    for post in my_posts:
        if post["id"] == id:
            my_posts.remove(post)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail= f"Post with id: {id} not found")

