from fastapi import APIRouter
from fastapi.openapi.models import Response

router = APIRouter()


@router.get("/")
async def root():
    return Response(
        status_code=200,
        detail='ok',
        result='working'
    )
