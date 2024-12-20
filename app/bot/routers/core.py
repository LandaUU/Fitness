from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.routers.weight.callback import WeightCallback
from app.bot.routers.steps.callback import StepsCallback
from app.bot.routers.measurements.callback import MeasureCallback
from app.bot.routers.fatsecret_reports.callback import FatSecretLoadFoodDiary, \
    FatSecretLoadFoodDiaryAction
from app.bot.routers.user.callback import UserCreateCallback, UserCreateAction
from app.bot.routers.reports.callback import ReportAction, ReportCallback

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Заполнить анкету",
                              callback_data=UserCreateCallback(action=UserCreateAction.begin).pack())],
    ])
    await message.answer("Привет! Я чат-бот [придумай название], буду твоим помощников на пути к стройности и" +
                         " здоровью. " +
                         "\nКогда начнем работу, тебе нужно будет каждый день отправлять отчеты о своем прогрессе, " +
                         "без них у нас ничего не выйдет. \nЕсли у тебя есть вопросы, можешь посмотреть видео,"
                         + " там более подробно о том, " +
                         "как взаимодействовать со мной. \n\nКак будешь готов(а)," +
                         f" нажми кнопку '{hbold('Заполнить анкету')}'", reply_markup=response_keyboard)


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
        [InlineKeyboardButton(text="Как ты сегодня кушал? (отчет)",
                              callback_data=FatSecretLoadFoodDiary(action=FatSecretLoadFoodDiaryAction.send).pack())],
        [InlineKeyboardButton(text="Открыть отчет за сегодня",
                              callback_data=ReportCallback(action=ReportAction.open_webapp).pack())]])
    await message.bot.send_message(chat_id=message.chat.id, text="Меню:", reply_markup=response_keyboard)
