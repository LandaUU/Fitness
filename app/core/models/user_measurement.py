from dataclasses import dataclass
from datetime import date


@dataclass
class UserMeasurement:
    id: int
    user_id: int
    pass_date: date
    weight: float
    steps: int
    neck: float
    waist: float
    stomach: float
    hips: float
    hip: float
    shin: float
    chest: float
    biceps: float
