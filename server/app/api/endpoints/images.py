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


router = APIRouter(prefix="/images")


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

    # use httpx to make a call to the server itself
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/")
    return response.json()
