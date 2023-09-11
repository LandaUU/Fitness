
from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import bot
from routers.weight.callback import WeightCallback

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
        [InlineKeyboardButton(text="Твой утренний вес?", callback_data=WeightCallback(test="set_weight").pack())],
        [InlineKeyboardButton(text="Сколько шагов сегодня прошел?", callback_data="set_steps")],
        [InlineKeyboardButton(text="Давай отправим твои замеры", callback_data="set_measurements")],
        [InlineKeyboardButton(text="Как ты сегодня кушал? (отчет)", callback_data="send_report_fs")]])
    await bot.send_message(chat_id=message.chat.id, text="Меню:", reply_markup=response_keyboard)
