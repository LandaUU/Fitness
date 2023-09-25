from aiogram.filters.callback_data import CallbackData


class UserCreateCallback(CallbackData, prefix="user"):
    is_first_report: bool
    final: bool
