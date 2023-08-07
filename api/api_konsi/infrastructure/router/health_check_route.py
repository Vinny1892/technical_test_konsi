from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check")
async def health_check():
    return {"message": "application works"}