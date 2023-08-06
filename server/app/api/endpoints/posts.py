from fastapi import APIRouter, Request
from models.connection import db
from models.post import Post

router = APIRouter(prefix="/posts")


@router.get("/")
def get_post():
    result = db["posts"].find({}, {"_id": 0})
    data = [item for item in result]
    return data


@router.post("/")
async def create_post(request: Request):
    try:
        request_body = await request.json()
    except ValueError:
        return {"error": "Invalid JSON data"}

    post = Post(imageUrl=request_body["imageUrl"],
                description=request_body["description"])
    post.save_to_collection()

    return {"data": "post created successfully"}
