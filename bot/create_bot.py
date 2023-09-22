from os import getenv
from aiogram import Bot

from aiogram.enums import ParseMode


def create_bot():
    TOKEN = getenv("BOT_TOKEN")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    return bot


bot = create_bot()
