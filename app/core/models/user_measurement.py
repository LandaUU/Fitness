from dataclasses import dataclass
from datetime import date


@dataclass
class UserMeasurement:
    user_id: int
    pass_date: date
    weight: float | None = None
    steps: int | None = None
    neck: float | None = None
    waist: float | None = None
    stomach: float | None = None
    hips: float | None = None
    hip: float | None = None
    shin: float | None = None
    chest: float | None = None
    biceps: float | None = None
