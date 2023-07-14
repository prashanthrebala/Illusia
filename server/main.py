from fastapi import FastAPI, Request
from dummyData import RESPONSE
import requests
from config import (
    IMAGE_GENERATION_ENDPOINT,
    X_RAPID_API_KEY,
    X_RAPID_API_HOST,
    DEFAULT_IMAGE_SIZE,
    DEFAULT_IMAGE_COUNT,
)

url = IMAGE_GENERATION_ENDPOINT

payload = {
    "prompt": "A cute baby sea otter",
    "n": DEFAULT_IMAGE_COUNT,
    "size": DEFAULT_IMAGE_SIZE
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": X_RAPID_API_KEY,
    "X-RapidAPI-Host": X_RAPID_API_HOST
}


app = FastAPI()


@app.get("/")
def root():
    return {"data": "Hello world"}


@app.post("/create")
async def create_new_image(request: Request):
    body = await request.json()
    print(body["prompt"])
    response = requests.post("url",
                             json={"prompt": body["prompt"],  "n": DEFAULT_IMAGE_COUNT,
                                   "size": DEFAULT_IMAGE_SIZE}, headers=headers)
    print(response.json())
    return "Hello"


@app.post("/images")
def get_images():
    print("!@!@")
    return RESPONSE
