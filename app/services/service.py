from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import UserData


async def get_user(session: AsyncSession):
    result = await session.execute(select(UserData).order_by(UserData.user_id))
    return result.scalars().all()
