import os

from sqlalchemy import MetaData
from sqlalchemy.orm import registry, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

app_engine = create_async_engine(
    "postgresql+asyncpg://{}:{}@{}:{}/{}".format(os.getenv('DB_USER'), os.getenv('DB_PASSWORD'),
                                                 os.getenv('DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_BASE')))

metadata_obj = MetaData()
mapper_registry = registry(metadata=metadata_obj)
Base: DeclarativeBase = mapper_registry.generate_base()
# async_sessionmaker: a factory for new AsyncSession objects.
# expire_on_commit - don't expire objects after transaction commit
async_session = async_sessionmaker(app_engine, expire_on_commit=False)


async def create_all_tables(engine: AsyncEngine, db_registry: registry) -> None:
    import app.db.sqlalchemy.models
    base = db_registry.generate_base()
    async with engine.begin() as conn:
        # print(await conn.run_sync(base.metadata.drop_all))
        print(await conn.run_sync(base.metadata.create_all))
        print('all tables created')
