import asyncio
import logging
import sys


from bot.routers.core import dp


async def main() -> None:
    from bot.create_bot import bot
    from bot.routers.register import register_routers
    register_routers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
