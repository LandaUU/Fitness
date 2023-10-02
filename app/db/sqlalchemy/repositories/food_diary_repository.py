from typing import Callable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.models.food_diary import FoodDiary


class FoodDiaryRepository:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self._session = session

    async def save_all(self, diary: list[FoodDiary]) -> None:
        async with self._session() as session:
            session.add_all(diary)
            await session.commit()

    async def save(self, diary: FoodDiary) -> None:
        async with self._session() as session:
            await session.merge(diary)
            await session.commit()

    async def get_diary(self, predicate: Callable) -> FoodDiary:
        async with self._session() as session:
            statement = select(FoodDiary).where(predicate(FoodDiary))
            return (await session.execute(statement)).scalar()

    async def get_list(self, predicate: Callable) -> list[FoodDiary]:
        async with self._session() as session:
            statement = select(FoodDiary).where(predicate(FoodDiary))
            return list((await session.execute(statement)).scalars())
