from dataclasses import dataclass
from datetime import date


@dataclass
class FoodDiary:
    id: int
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
    calcium: float
    cholesterol: float
    fiber: float
    iron: float
    monounsaturated_fat: float
    polyunsaturated_fat: float
    potassium: float
    saturated: float
    sodium: float
    sugar: float
    vitamin_a: float
    vitamin_c: float
    trans_fat: float
