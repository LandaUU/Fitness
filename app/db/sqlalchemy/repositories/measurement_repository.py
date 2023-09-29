from typing import Callable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.models.user_measurement import UserMeasurement 


class MeasurementRepository:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self._session = session

    async def save(self, measurement: UserMeasurement) -> None:
        async with self._session() as session:
            await session.merge(measurement)
            await session.commit()

    async def get_measurement(self, predicate: Callable) -> UserMeasurement:
        async with self._session() as session:
            statement = select(UserMeasurement).where(predicate(UserMeasurement))
            return (await session.execute(statement)).scalar()
        