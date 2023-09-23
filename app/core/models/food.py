from dataclasses import dataclass


@dataclass
class Food:
    id: int
    name: str
    category_id: int
