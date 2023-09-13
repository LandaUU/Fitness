
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import bot
from routers.weight.callback import WeightCallback
from routers.steps.callback import StepsCallback
from routers.measurements.callback import MeasureCallback
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("menu"))
async def command_menu_handler(message: Message) -> None:
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Твой утренний вес?",
                              callback_data=WeightCallback(chat_id=message.chat.id,
                                                           user_id=message.from_user.id).pack())],
        [InlineKeyboardButton(text="Сколько шагов сегодня прошел?",
                              callback_data=StepsCallback(chat_id=message.chat.id,
                                                          user_id=message.from_user.id).pack())],
        [InlineKeyboardButton(text="Давай отправим твои замеры",
                              callback_data=MeasureCallback(chat_id=message.chat.id,
                                                            user_id=message.from_user.id).pack())],
        [InlineKeyboardButton(text="Как ты сегодня кушал? (отчет)", callback_data="send_report_fs")]])
    await bot.send_message(chat_id=message.chat.id, text="Меню:", reply_markup=response_keyboard)
