from fastapi import APIRouter, Request
from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from uuid import uuid4

from utils.config import IMAGE_KIT_PRIVATE_KEY, IMAGE_KIT_PUBLIC_KEY, IMAGE_KIT_URL_ENDPOINT

router = APIRouter(prefix="/imagekit")

imagekit = ImageKit(
    private_key=IMAGE_KIT_PRIVATE_KEY,
    public_key=IMAGE_KIT_PUBLIC_KEY,
    url_endpoint=IMAGE_KIT_URL_ENDPOINT
)


@router.get("/")
def get_post():
    return {"data": "/posts GET reached"}


@router.post("/upload")
async def create_post(request: Request):
    try:
        request_body = await request.json()
    except ValueError:
        return {"error": "Invalid JSON data"}

    try:
        file_url = request_body["imageUrl"]
        file_name = str(uuid4())
        folder = '/illusia/store'

        imagekit_response = imagekit.upload_file(
            file=file_url,
            file_name=file_name,
            options=UploadFileRequestOptions(folder=folder)
        )

        meta_data = imagekit_response.response_metadata.raw
        return {"url": meta_data["url"], "thumbnailUrl": meta_data["thumbnailUrl"]}
    except Exception:
        return {"error": "Something went wrong while uploading"}
