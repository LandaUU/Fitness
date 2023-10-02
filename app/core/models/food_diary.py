from dataclasses import dataclass
from datetime import date


@dataclass
class FoodDiary:
    food_id: int
    user_id: int
    meal_id: int
    diary_date: date
    amount: float
    metric_type: int
    calories: float
    protein: float
    fat: float
    carbohydrate: float
    id: int | None = None
    calcium: float | None = None
    cholesterol: float | None = None
    fiber: float | None = None
    iron: float | None = None
    monounsaturated_fat: float | None = None
    polyunsaturated_fat: float | None = None
    potassium: float | None = None
    saturated: float | None = None
    sodium: float | None = None
    sugar: float | None = None
    vitamin_a: float | None = None
    vitamin_c: float | None = None
    trans_fat: float | None = None
