from datetime import datetime, date

from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton, WebAppInfo,  \
    InlineQueryResultsButton, CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext

from app.db.sqlalchemy.base import async_session
from bot.routers.fatsecret_reports.callback import FatSecretUserSyncCallback, FatSecretUserSyncAction, \
    FatSecretLoadFoodDiary, FatSecretLoadFoodDiaryAction
from bot.routers.fatsecret_reports.states import FsReportState
from app.modules.fatsecret.client import fatsecret_client
from app.db.sqlalchemy.repositories.user_repository import UserRepository
from app.controllers.fatsecret_reports import save_user_report

fatsecret_router = Router(name="fatsecret")


@fatsecret_router.callback_query(FatSecretUserSyncCallback.filter(F.action == FatSecretUserSyncAction.begin))
async def callback_router(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await state.set_state(FsReportState.pin_code)
    auth_url = fatsecret_client.get_authorize_url()
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text=f"Ссылка для синхронизации аккаунта: {auth_url}")
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text="Введи код:")
    await query.answer()


@fatsecret_router.message(FsReportState.pin_code)
async def get_user_pin_code(message: Message, state: FSMContext):
    pin_code = message.text
    session_token = fatsecret_client.get_user_oauth(pin_code)

    repository = UserRepository(session=async_session)

    stored_user = await repository.get_user(lambda user: user.telegram_id == message.from_user.id)

    stored_user.oauth_token, stored_user.oauth_secret = session_token

    stored_user.oauth_date = date.today()

    await repository.save(stored_user)

    await message.bot.send_message(chat_id=message.chat.id,
                                   text="Мы все настроили и готовы полноценно работать. Завтра жду твой первый отчет.")


@fatsecret_router.callback_query(FatSecretLoadFoodDiary.filter(F.action == FatSecretLoadFoodDiaryAction.begin))
async def get_food_diary_callback_begin(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Отправить отчёт",
                              callback_data=FatSecretUserSyncCallback(action=FatSecretUserSyncAction.begin).pack())]])

    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Давай отправим твой отчет по питанию',
                                 reply_markup=response_keyboard)


@fatsecret_router.callback_query(FatSecretLoadFoodDiary.filter(F.action == FatSecretLoadFoodDiaryAction.send))
async def get_food_diary_callback_send(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    repository = UserRepository(session=async_session)
    stored_user = await repository.get_user(lambda user: user.telegram_id == query.from_user.id)
    if stored_user is None:
        await query.bot.send_message(chat_id=query.message.chat.id,
                                     text='Вы не зарегистрированы, введите `/start` для начала работы')

    reply_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=False, keyboard=[[KeyboardButton(
        text='Выбрать дату', web_app=WebAppInfo(url='http://127.0.0.1:5173/date_picker'))]])

    await query.answer()
    await query.bot.send_message(chat_id=query.message.chat.id, text="Выберите дату для выгрузки отчета",
                                 reply_markup=reply_keyboard)


def check_get_date_step(message: Message) -> bool:
    return message.web_app_data.button_text == 'Выбрать дату'


@fatsecret_router.message(check_get_date_step)
async def general_message_handler(message: Message):
    date = message.web_app_data.data

    repository = UserRepository(session=async_session)
    stored_user = await repository.get_user(lambda user: user.telegram_id == message.from_user.id)
    if stored_user is None:
        await message.bot.send_message(chat_id=message.chat.id,
                                       text='Вы не зарегистрированы, введите `/start` для начала работы')

    await save_user_report(user=stored_user, diary_date=datetime.strptime(date, '%Y-%m-%d'))

    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Отчет успешно отправлен')
