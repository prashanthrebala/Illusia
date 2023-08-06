from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.imagekit import router as imagekit_router
from api.endpoints.images import router as images_router
from api.endpoints.posts import router as posts_router
from utils.dummyData import RESPONSE


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
app.include_router(imagekit_router)
app.include_router(images_router)
app.include_router(posts_router)


@app.get("/")
def root():
    return {"data": "Hello world"}
