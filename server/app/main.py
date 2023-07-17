from fastapi import FastAPI
from api.endpoints.imagekit import router as imagekit_router
from api.endpoints.images import router as images_router
from api.endpoints.posts import router as posts_router
from utils.dummyData import RESPONSE


app = FastAPI()
app.include_router(imagekit_router)
app.include_router(images_router)
app.include_router(posts_router)


@app.get("/")
def root():
    return {"data": "Hello world"}
