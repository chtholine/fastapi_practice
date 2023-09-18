from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return dict(
        status_code=200,
        detail='ok',
        result='working'
    )
