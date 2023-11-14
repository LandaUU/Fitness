from aiogram.fsm.state import StatesGroup, State


class FoodDiaryRequestState(StatesGroup):
    target_user = State()
