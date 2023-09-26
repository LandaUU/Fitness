import asyncio
import logging
import sys
import sqlalchemy.orm

from bot.routers.core import dp
from app.db.sqlalchemy.base import create_all_tables

async def main() -> None:
    from bot.create_bot import bot
    from bot.routers.register import register_routers
    register_routers()
    await create_all_tables()
    await sqlalchemy.orm.configure_mappers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
