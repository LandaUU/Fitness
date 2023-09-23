from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from bot.routers.fatsecret_reports.callback import FsReportCallback
from bot.routers.fatsecret_reports.states import FsReportState
from app.modules.fatsecret.client import fatsecret_client

fatsecret_router = Router(name="fatsecret")


@fatsecret_router.callback_query(FsReportCallback.filter())
async def callback_router(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await state.set_state(FsReportState.pin_code)
    auth_url = fatsecret_client.get_authorize_url()
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text=f"Ссылка для синхронизации аккаунта: {auth_url}")
    await query.answer()


@fatsecret_router.message(Command("load_fatsecret_report"))
async def command_router(message: Message, state: FSMContext):
    await state.set_state(FsReportState.pin_code)
    auth_url = fatsecret_client.get_authorize_url()
    await message.bot.send_message(chat_id=message.chat.id,
                                   text=f"Ссылка для синхронизации аккаунта: {auth_url}")


@fatsecret_router.message(FsReportState.pin_code)
async def get_user_pin_code(message: Message, state: FSMContext):
    pin_code = message.text
    session_token = fatsecret_client.get_user_oauth(pin_code)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text="Всё получилось, спасибо!")
