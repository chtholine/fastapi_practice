from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.database import get_postgres
from app.db.models import Users
from app.schemas.schemas import UserSchema
from app.services.redis_service import get_redis
from app.utils.logger_conf import logger

router = APIRouter()


@router.get("/")
async def healthcheck():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }


@router.post("/users/")
async def create_user(user_data: UserSchema, session: AsyncSession = Depends(get_postgres)):
    try:
        logger.info("Creating a new user")
        new_user = Users(
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
        logger.info("User created successfully")
        return new_user
    except Exception as e:
        logger.error(f"Error creating a user: {str(e)}")
        return JSONResponse(content={"message": f"Error creating a user: {str(e)}"}, status_code=500)


@router.get("/users/")
async def read_users(session: AsyncSession = Depends(get_postgres)):
    try:
        logger.info("Fetching user data")
        result = await session.execute(select(Users))
        users = result.scalars().all()
        logger.info("User data successfully fetched")
        return {"users": users}
    except Exception as e:
        logger.error(f"Error fetching user data: {str(e)}")
        return JSONResponse(content={"message": f"Error fetching user data: {str(e)}"}, status_code=500)


@router.get("/test-redis/")
async def test_redis():
    try:
        redis = await get_redis()
        await redis.ping()
        await redis.close()
        logger.info("Redis connection is successful.")
        return JSONResponse(content={
            "message": "Redis connection is successful."
        })
    except aioredis.RedisError as e:
        logger.error(f"Redis connection failed: {str(e)}.")
        return JSONResponse(content={
            "message": f"Redis connection failed: {str(e)}."
        })


@router.get("/test-postgres/")
async def test_postgres(session: AsyncSession = Depends(get_postgres)):
    try:
        result = await session.execute(select(1))
        result.scalar()
        logger.info("PostgreSQL connection is successful.")
        return JSONResponse(content={
            "message": "PostgreSQL connection is successful."
        })
    except Exception as e:
        logger.error(f"PostgreSQL connection failed: {str(e)}.")
        return JSONResponse(content={
            "message": f"PostgreSQL connection failed: {str(e)}."
        })
