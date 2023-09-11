from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from routers.weight.callback import WeightCallback

weight_router = Router(name="weight")


@weight_router.callback_query(WeightCallback.filter())
async def callback_router(query: CallbackQuery, callback_data):
    await query.bot.send_message(chat_id=query.message.chat.id, text="Такс, записал")
    await query.answer()


@weight_router.message(Command("set_weight"))
async def command_router(message: Message):
    await message.reply(text='Ага, ага, записал')
