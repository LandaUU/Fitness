from aiogram.filters.callback_data import CallbackData


class WeightCallback(CallbackData, prefix="weight"):
    user_id: int
    chat_id: int
