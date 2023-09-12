from aiogram.filters.callback_data import CallbackData


class StepsCallback(CallbackData, prefix="steps"):
    chat_id: int
    user_id: int
