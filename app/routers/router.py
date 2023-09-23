
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import service
from app.db.database import get_session

router = APIRouter()


class CitySchema(BaseModel):
    name: str
    population: int


@router.get("/")
async def healthcheck():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }


@router.get("/cities/biggest", response_model=list[CitySchema])
async def get_biggest_cities(session: AsyncSession = Depends(get_session)):
    cities = await service.get_biggest_cities(session)
    return [CitySchema(name=c.name, population=c.population) for c in cities]


@router.post("/cities/")
async def add_city(city: CitySchema, session: AsyncSession = Depends(get_session)):
    city = service.add_city(session, city.name, city.population)
    await session.commit()
    return city
