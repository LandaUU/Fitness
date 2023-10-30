from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, \
    InlineKeyboardButton, WebAppInfo
from aiogram.filters.callback_data import CallbackData
from aiogram.filters import Command
from app.db.sqlalchemy.repositories.user_repository import UserRepository

from bot.routers.admin.callback import AdminAction, AdminCallback
from app.db.sqlalchemy.base import async_session

admin_router = Router(name="admin")


@admin_router.message(Command("admin"))
async def handle_admin_command(message: Message):
    repository = UserRepository(session=async_session)
    stored_user = await repository.get_user(lambda user: user.telegram_id == message.from_user.id)
    if not stored_user.admin:
        await message.bot.send_message(chat_id=message.chat.id,
                                       text='Большая сила - это большая ответственность © Дядюшка Бен')
        return

    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Настроить расписание задач",
                              callback_data=AdminCallback(action=AdminAction.configure_jobs).pack())],
        [InlineKeyboardButton(text="Запросить пищевой отчет у пользователя",
                              callback_data=AdminCallback(action=AdminAction.request_food_diary).pack())],
        [InlineKeyboardButton(text="Запросить замеры у пользователя",
                              callback_data=AdminCallback(action=AdminAction.request_measurement).pack())],
        [InlineKeyboardButton(text="Посмотреть отчет пользователя",
                              callback_data=AdminCallback(action=AdminAction.view_food_diary).pack())],
        [InlineKeyboardButton(text="Посмотреть замеры пользователя",
                              callback_data=AdminCallback(action=AdminAction.view_measurement).pack())]])
    await message.bot.send_message(chat_id=message.chat.id, text="Действия (админ):", reply_markup=response_keyboard)


@admin_router.callback_query(AdminCallback.filter(F.action == AdminAction.configure_jobs))
async def configure_jobs(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await query.answer()
    await query.bot.send_message(text='''Пока что этот функционал не доступен.
Задачи запускаются по расписанию:
1) запросы по пищевым дневникам отправляются пользователям каждый день в 19 часов
2) запросы по замерам отправляются каждую субботу в 9 утра''',
                                 chat_id=query.message.chat.id)


@admin_router.callback_query(AdminCallback.filter(F.action == AdminAction.request_food_diary))
async def request_food_diary(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(web_app=WebAppInfo(url='http://127.0.0.1:5173/'),
                             text='Открыть отчёт')]])

    await query.answer(text='Выберите из списка пользователей того, чей пищевой отчет хотите запросить:')
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Выбор пользователя:',
                                 reply_markup=response_keyboard)


@admin_router.callback_query(AdminCallback.filter(F.action == AdminAction.request_measurement))
async def request_measurement(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(web_app=WebAppInfo(url='http://127.0.0.1:5173/'),
                             text='Открыть отчёт')]])

    await query.answer(text='Выберите из списка пользователей того, чьи замеры хотите запросить:')
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Выбор пользователя:',
                                 reply_markup=response_keyboard)


@admin_router.callback_query(AdminCallback.filter(F.action == AdminAction.view_food_diary))
async def view_food_diary(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(web_app=WebAppInfo(url='http://127.0.0.1:5173/'),
                             text='Открыть отчёт')]])

    await query.answer(text='Выберите из списка пользователей того, чей отчет хотите посмотреть:')
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Выбор пользователя:',
                                 reply_markup=response_keyboard)


@admin_router.callback_query(AdminCallback.filter(F.action == AdminAction.view_measurement))
async def view_measurement(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(web_app=WebAppInfo(url='http://127.0.0.1:5173/'),
                             text='Открыть отчёт')]])

    await query.answer(text='Выберите из списка пользователей того, чьи замеры хотите посмотреть:')
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Выбор пользователя:',
                                 reply_markup=response_keyboard)
