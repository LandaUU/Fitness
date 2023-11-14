from datetime import datetime
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from app.bot.routers.fatsecret_reports.callback import FatSecretUserSyncAction, FatSecretUserSyncCallback
from app.db.sqlalchemy.repositories.repository import EntityRepository
from app.db.sqlalchemy.models.food_diary import FoodDiary

from app.bot.routers.admin.callback import AdminAction, AdminCallback
from app.db.sqlalchemy.base import async_session

rfd_router = Router()


@rfd_router.callback_query(AdminCallback.filter(F.action == AdminAction.request_food_diary))
async def request_food_diary(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    response_keyboard = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(web_app=WebAppInfo(url='http://127.0.0.1:5173/user_picker'),
                       text='Выбрать пользователя')]])

    await query.answer(text='Выберите из списка пользователей того, чей пищевой отчет хотите запросить:')
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Кнопка',
                                 reply_markup=response_keyboard)


def check_get_user_step(message: Message) -> bool:
    return message.web_app_data and message.web_app_data.button_text == 'Выбрать пользователя'


def check_get_date_step(message: Message) -> bool:
    return message.web_app_data and message.web_app_data.button_text == 'Выбрать дату'


@rfd_router.message(check_get_user_step)
async def request_food_diary_date(message: Message, state: FSMContext):
    print(message.web_app_data.data)

    user_id = message.web_app_data.data

    await state.set_state({'target_user': user_id})

    reply_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, is_persistent=False, keyboard=[[KeyboardButton(
        text='Выбрать дату', web_app=WebAppInfo(url='http://127.0.0.1:5173/date_picker'))]])

    await message.bot.send_message(chat_id=message.chat.id, text="Выберите дату для выгрузки отчета",
                                   reply_markup=reply_keyboard)


@rfd_router.message(check_get_date_step)
async def request_food_diary_final(message: Message, state: FSMContext):
    print(message.web_app_data.data)

    date: str = message.web_app_data.data

    target_user = (await state.get_state())['target_user']

    repository = EntityRepository(async_session, FoodDiary)

    diary = repository.get(lambda fd: fd.user_id == target_user and fd.diary_date ==
                           datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))

    if diary is not None:
        await message.bot.send_message(chat_id=message.chat.id, text='Пользователь уже отправил отчет')
        return

    await message.bot.send_message(chat_id=target_user,
                                   text=f'Дружочек-пирожочек, пора сдавать отчет по питанию за {date}. '
                                   'Для этого нажми на кнопку "Отправить отчет" и следуй инструкции')

    response_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Отправить отчёт",
                        callback_data=FatSecretUserSyncCallback(action=FatSecretUserSyncAction.begin).pack())]])

    await message.bot.send_message(chat_id=target_user,
                                   text='Давай отправим твой отчет по питанию',
                                   reply_markup=response_keyboard)
