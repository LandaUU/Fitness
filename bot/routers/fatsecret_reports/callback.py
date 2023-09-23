from aiogram.filters.callback_data import CallbackData


class FsReportCallback(CallbackData, prefix="fatsecret"):
    user_id: int
    chat_id: int
