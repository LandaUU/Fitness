import asyncio

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.core.models.user import User
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.repository import EntityRepository
from app.bot.create_bot import create_bot
from app.bot.routers.fatsecret_reports.callback import FatSecretLoadFoodDiary, FatSecretLoadFoodDiaryAction


async def send_choose_date_message(bot: Bot, chat_id: int):
    reply_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Сдать отчет",
                             callback_data=FatSecretLoadFoodDiary(action=FatSecretLoadFoodDiaryAction.send).pack())]])

    await bot.send_message(chat_id=chat_id, text="Привет, готов(а) сдать отчет по питанию?",
                           reply_markup=reply_keyboard)


async def send_food_diary_request():
    import app.db.sqlalchemy.models
    bot = create_bot()

    repository = EntityRepository(async_session, User)

    users: list[User, None] = await repository.all()

    for user in users:
        await send_choose_date_message(bot, user.telegram_id)


asyncio.run(send_food_diary_request())
