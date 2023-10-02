from aiogram.filters.callback_data import CallbackData

from enum import StrEnum, auto


class ReportAction(StrEnum):
    open_webapp = auto()
    close_webapp = auto()


class ReportCallback(CallbackData, prefix="fatsecret"):
    action: ReportAction
