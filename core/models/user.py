
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: int
    fio: str
    lastname: str
    middlename: str
    firstname: str
    height: float
    age: int
    birthday: date
    gender: str
    pay_date: date
    next_report_date: date
    exit_date: date
    oauth_token: str
    oauth_secret: str
    oauth_date: date
