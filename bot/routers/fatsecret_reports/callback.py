from aiogram.filters.callback_data import CallbackData

from enum import StrEnum, auto


class FatSecretUserSyncAction(StrEnum):
    begin = auto()
    send_auth_link = auto()
    fetch_user_oauth1_session = auto()
    save_user_oauth1_session = auto()
    clear = auto()


class FatSecretUserSyncCallback(CallbackData, prefix="fatsecret"):
    action: FatSecretUserSyncAction
