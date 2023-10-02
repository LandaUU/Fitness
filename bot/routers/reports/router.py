from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from bot.routers.reports.callback import ReportCallback, ReportAction

reports = Router(name="app_reports")


@reports.callback_query(ReportCallback.filter(F.action == ReportAction.open_webapp))
async def callback_router(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Ваш отчёт за сегодня:',
                                 reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                                     InlineKeyboardButton(web_app=WebAppInfo(url='https://google.com'),
                                                          text='Открыть отчёт')]]))
