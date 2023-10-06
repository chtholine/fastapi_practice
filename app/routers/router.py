from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from redis import asyncio as aioredis
from app.core.config import Settings
from app.db.database import get_session
from app.db.models import UserData

router = APIRouter()


async def get_redis():
    return await aioredis.from_url(
        Settings.REDIS_URL
    )


class UserSchema(BaseModel):
    user_email: str
    user_firstname: str
    user_lastname: str
    user_status: str
    user_city: str
    user_phone: str
    user_links: str
    user_avatar: str
    hashed_password: str
    is_superuser: bool


@router.get("/")
async def healthcheck():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }


@router.post("/users/")
async def create_user(user_data: UserSchema, session: AsyncSession = Depends(get_session)):
    new_user = UserData(
        user_email=user_data.user_email,
        user_firstname=user_data.user_firstname,
        user_lastname=user_data.user_lastname,
        user_status=user_data.user_status,
        user_city=user_data.user_city,
        user_phone=user_data.user_phone,
        user_links=user_data.user_links,
        user_avatar=user_data.user_avatar,
        hashed_password=user_data.hashed_password,
        is_superuser=user_data.is_superuser,
    )
    session.add(new_user)
    await session.commit()  # Commit the transaction to get the new_user.id
    await session.refresh(new_user)
    return new_user


@router.get("/users/")
async def read_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(UserData))
    users = result.scalars().all()
    return {"users": users}
