from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    fio: str
    height: float
    age: int
    gender: str
    id: Optional[int] = None
    lastname: Optional[str] = None
    middlename: Optional[str] = None
    firstname: Optional[str] = None
    birthday: Optional[date] = None
    telegram_id: Optional[int] = None
    telegram_username: Optional[str] = None
    pay_date: Optional[date] = None
    next_report_date: Optional[date] = None
    exit_date: Optional[date] = None
    oauth_token: Optional[str] = None
    oauth_secret: Optional[str] = None
    oauth_date: Optional[date] = None
