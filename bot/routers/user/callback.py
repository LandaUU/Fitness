from aiogram.filters.callback_data import CallbackData

from enum import StrEnum, auto


class UserCreateAction(StrEnum):
    begin = auto()
    edit = auto()
    fio = auto()
    age = auto()
    gender = auto()
    height = auto()
    physical_level = auto()
    sickness = auto()
    losing_weight_level = auto()
    losing_weight_in_half_year_level = auto()
    check = auto()
    save = auto()
    clear = auto()


class UserCreateCallback(CallbackData, prefix="user"):
    action: UserCreateAction
