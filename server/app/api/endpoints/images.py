from fastapi import APIRouter, Request

router = APIRouter(prefix="/images")


@router.post("/create")
async def create_image(request: Request):
    data = await request.json()
    print(data)
