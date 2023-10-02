from dataclasses import dataclass


@dataclass
class Meal:
    name: str
    id: int | None = None
