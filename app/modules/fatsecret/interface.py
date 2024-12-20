from abc import abstractmethod
from app.core.models.food_diary import FoodDiary

from typing import Protocol, Tuple


class IClient(Protocol):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_user_report(self, user, diary_date) -> list[FoodDiary]:
        raise NotImplementedError()

    @abstractmethod
    def get_authorize_url(self, callback_url: str = 'oob') -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_user_oauth(self, pin) -> Tuple[str, str]:
        raise NotImplementedError()

    @abstractmethod
    def get_food_details(self, food_id) -> dict:
        raise NotImplementedError()
