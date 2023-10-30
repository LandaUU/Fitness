from aiogram.filters.callback_data import CallbackData

from enum import StrEnum, auto


class AdminAction(StrEnum):
    configure_jobs = auto()
    request_food_diary = auto()
    request_measurement = auto()
    view_food_diary = auto()
    view_measurement = auto()


class RequestUserFoodDiaryAction(StrEnum):
    choose_user: auto()
    choose_date: auto()


class AdminCallback(CallbackData, prefix="admin"):
    action: AdminAction


class RequestUserFoodDiary(CallbackData, prefix='admin_request_food'):
    action: RequestUserFoodDiaryAction
