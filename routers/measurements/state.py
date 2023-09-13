from aiogram.fsm.state import StatesGroup, State


class MeasureState(StatesGroup):
    Neck = State()  # Шея
    Waist = State()  # Талия
    Stomach = State()  # Живот
    Hips = State()  # Бедра
    Hip = State()  # Бедро
    Shin = State()  # Голень
    Chest = State()  # Грудь
    Biceps = State()  # Бицепс
