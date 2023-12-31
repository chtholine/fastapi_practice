from redis import asyncio as aioredis

from app.core.config import settings

pool = aioredis.ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


async def get_redis():
    return aioredis.Redis(connection_pool=pool)
