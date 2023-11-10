from os import getenv
from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TEST

from aiogram.enums import ParseMode


def create_bot():
    TOKEN = getenv("BOT_TOKEN")
    session = AiohttpSession(
        api=TEST
    )
    match getenv("BOT_ENV"):
        case 'production':
            bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
        case 'test':
            bot = Bot(TOKEN, parse_mode=ParseMode.HTML, session=session)

    return bot


bot = create_bot()
