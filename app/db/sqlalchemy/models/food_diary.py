from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, REAL, INTEGER, DATE
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.food_diary import FoodDiary


food_diary = Table(
    "food_diary",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("food_id", INTEGER, ForeignKey("food.id")),
    Column("user_id", INTEGER, ForeignKey("user.id")),
    Column("meal_id", INTEGER, ForeignKey("meal.id")),
    Column("diary_date", DATE),
    Column("amount", INTEGER),
    Column("metric_type", VARCHAR),
    Column("calories", REAL),
    Column("protein", REAL),
    Column("fat", REAL),
    Column("carbohydrate", REAL),
    Column("calcium", REAL),
    Column("cholesterol", REAL),
    Column("fiber", REAL),
    Column("iron", REAL),
    Column("monounsaturated_fat", REAL),
    Column("polyunsaturated_fat", REAL),
    Column("trans_fat", REAL),
    Column("potassium", REAL),
    Column("saturated", REAL),
    Column("sodium", REAL),
    Column("sugar", REAL),
    Column("vitamin_a", REAL),
    Column("vitamin_c", REAL),
)

mapper_registry.map_imperatively(
    FoodDiary,
    food_diary,
)
