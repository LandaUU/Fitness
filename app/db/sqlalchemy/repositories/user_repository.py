from typing import Callable
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.core.models.user import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create_user(self, user: User) -> None:
        self._session.merge(user)
        self._session.commit()

    def get_user(self, predicate: Callable) -> User:
        statement = select(User).where(predicate)
        return self._session.execute(statement).scalar_one()
