from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import REAL, BIGINT, DATE, INTEGER
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.food_diary import FoodDiary


food_diary = Table(
    "food_diary",
    metadata_obj,
    Column("id", BIGINT, primary_key=True),
    Column("food_id", BIGINT, ForeignKey("food.id")),
    Column("user_id", BIGINT, ForeignKey("user.id")),
    Column("meal_id", BIGINT, ForeignKey("meal.id")),
    Column("diary_date", DATE),
    Column("amount", INTEGER),
    Column("metric_type", INTEGER),
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
