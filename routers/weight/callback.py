from aiogram.filters.callback_data import CallbackData


class WeightCallback(CallbackData, prefix="testcbdata"):
    test: str
