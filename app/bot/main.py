import asyncio
import logging
import sys

from app.bot.routers.core import dp
from app.db.sqlalchemy.base import create_all_tables
from app.db.sqlalchemy.base import app_engine, mapper_registry
from app.bot.create_bot import bot
from app.bot.routers.register import register_routers


async def main() -> None:
    register_routers()
    await create_all_tables(app_engine, mapper_registry)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
