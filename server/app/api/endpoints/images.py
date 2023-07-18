from fastapi import APIRouter, Request
from utils.config import (
    IMAGE_GENERATION_ENDPOINT,
    X_RAPID_API_KEY,
    X_RAPID_API_HOST,
    DEFAULT_IMAGE_SIZE,
    DEFAULT_IMAGE_COUNT,
)
import requests
import httpx
from models.post import Post
from utils.dummyData import RESPONSE

router = APIRouter(prefix="/images")

OPENAI = False


@router.post("/create")
async def create_image(request: Request):
    try:
        request_body = await request.json()
    except ValueError:
        return {"error": "Invalid JSON data"}

    prompt = request_body.get("prompt")
    if not prompt:
        return {"error": "Missing 'prompt' value"}

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": X_RAPID_API_KEY,
        "X-RapidAPI-Host": X_RAPID_API_HOST
    }
    payload = {
        "prompt": prompt,
        "n": DEFAULT_IMAGE_COUNT,
        "size": DEFAULT_IMAGE_SIZE
    }

    if OPENAI:
        print("obtaining response from open ai")
        response = requests.post(
            url=IMAGE_GENERATION_ENDPOINT, headers=headers, json=payload)

        response_json = response.json()
    else:
        print("obtaining local response")
        response_json = RESPONSE

    generated_image_url = response_json["data"][0]["url"]
    print(generated_image_url)

    # use httpx to make a call to the server itself
    async with httpx.AsyncClient() as client:
        # upload image to imagekit
        imagekit_response = await client.post(
            "http://localhost:8001/imagekit/upload",
            json={"imageUrl": generated_image_url}
        )

        imagekit_response_json = imagekit_response.json()

        # create post in mongodb
        create_post_response = await client.post(
            "http://localhost:8001/posts/",
            json={
                "imageUrl": imagekit_response_json["url"], "description": prompt}
        )

    return {
        "imageUrl": imagekit_response_json["url"],
        "description": prompt
    }
