from aiogram.filters.callback_data import CallbackData


class MeasureCallback(CallbackData, prefix="measure"):
    chat_id: int
    user_id: int
