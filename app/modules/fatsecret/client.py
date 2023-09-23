import os
from datetime import date
from typing import Tuple
from app.core.models.food_diary import FoodDiary
from app.modules.fatsecret.interface import IClient
from fatsecret import Fatsecret


class FsClient(IClient):
    def __init__(self, consumer_key, consumer_secret) -> None:
        self._client = Fatsecret(consumer_key=consumer_key,
                                 consumer_secret=consumer_secret)

    def _change_user_session(self, user_session: Tuple[str, str]) -> None:
        self._client.access_token = user_session[0]
        self._client.access_token_secret = user_session[1]
        self._client.session = self._client.oauth.get_session(token=user_session)

    def get_authorize_url(self, callback_url: str = 'oob') -> str:
        return self._client.get_authorize_url(callback_url=callback_url)

    def get_user_oauth(self, pin: str) -> Tuple[str, str]:
        return self._client.authenticate(pin)

    def get_user_report(self, user_session: Tuple[str, str], diary_date: date) -> FoodDiary:
        self._change_user_session(user_session)
        return self._client.food_entries_get(date=diary_date)

    def get_food_details(self) -> dict:
        pass


fatsecret_client = FsClient(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
