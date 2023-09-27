from typing import Callable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.models.user import User


class UserRepository:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self._session = session

    async def save(self, user: User) -> None:
        async with self._session() as session:
            await session.merge(user)
            await session.commit()

    async def get_user(self, predicate: Callable) -> User:
        async with self._session() as session:
            statement = select(User).where(predicate(User))
            return (await session.execute(statement)).scalar()
