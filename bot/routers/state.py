"""
Здесь хранится глобальное состояние приложения
"""
from enum import StrEnum, auto

from aiogram.fsm.state import StatesGroup, State


# ToDo: Если у нас несколько пользователей, работает ли из коробки принцип state per user?


class BotActions(StrEnum):
    user_not_authorized = auto()
    fill_user_report = auto()
    user_authorized = auto()
    fill_food_diary = auto()
    fill_measurement = auto()
    fill_weight = auto()
    fill_steps = auto()


class BotState(StatesGroup):
    action = State()
