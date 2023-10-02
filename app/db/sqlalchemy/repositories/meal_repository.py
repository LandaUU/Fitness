from typing import Callable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.models.meal import Meal


class MealRepository:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self._session = session

    async def save(self, meal: Meal) -> None:
        async with self._session() as session:
            await session.merge(meal)
            await session.commit()

    async def get(self, predicate: Callable) -> Meal:
        async with self._session() as session:
            statement = select(Meal).where(predicate(Meal))
            return (await session.execute(statement)).scalar()
