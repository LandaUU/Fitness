from typing import Callable, Generic, TypeVar, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

T = TypeVar('T')


class EntityRepository:
    def __init__(self, session: async_sessionmaker[AsyncSession], entity_type: T) -> None:
        self._session = session
        self._entity_type = entity_type

    async def save(self, entity: Generic[T]) -> None:
        async with self._session() as session:
            await session.merge(entity)
            await session.commit()

    async def get(self, predicate: Callable) -> Generic[T]:
        async with self._session() as session:
            statement = select(self._entity_type).where(predicate(self._entity_type))
            return (await session.execute(statement)).scalar()

    async def all(self, predicate: Optional[Callable] = None) -> list[Generic[T]]:
        async with self._session() as session:
            if predicate:
                statement = select(self._entity_type).where(predicate(self._entity_type))
            else:
                statement = select(self._entity_type)
            return list(map(lambda sql_tuple: sql_tuple[0], (await session.execute(statement)).all()))
