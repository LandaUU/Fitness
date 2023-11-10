import asyncio

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.core.models.user import User
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.repository import EntityRepository
from app.bot.create_bot import create_bot
from app.bot.routers.measurements.callback import MeasureCallback


async def send_choose_date_message(bot: Bot, chat_id: int):
    reply_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Отправить замеры",
                             callback_data=MeasureCallback(chat_id=chat_id,
                                                           user_id=chat_id).pack())]])

    await bot.send_message(chat_id=chat_id, text="Круто, мы отследили твой образ жизни и пищевой дневник," +
                                                 " а это значит пришло время сделать повторные замеры")
    await bot.send_message(chat_id=chat_id, text='Завтра утром на тощак сделай вот такие замеры, вернись сюда' +
                                                 ' и тыкни на кнопочку ниже. До встречи',
                           reply_markup=reply_keyboard)


async def send_user_measurement_request():
    import app.db.sqlalchemy.models
    bot = create_bot()

    repository = EntityRepository(async_session, User)

    users: list[User, None] = await repository.all()

    for user in users:
        await send_choose_date_message(bot, user.telegram_id)


asyncio.run(send_user_measurement_request())
