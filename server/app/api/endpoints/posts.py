from fastapi import APIRouter

router = APIRouter(prefix="/posts")


@router.get("/")
def create_image():
    return {"data": "/posts GET reached"}


@router.post("/")
async def create_image():
    return {"data": "/posts POST reached"}
