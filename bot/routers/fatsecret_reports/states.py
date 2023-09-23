from aiogram.fsm.state import StatesGroup, State


class FsReportState(StatesGroup):
    pin_code = State()
