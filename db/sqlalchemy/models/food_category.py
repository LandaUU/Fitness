from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy import Table
from db.sqlalchemy.mapper_registry import mapper_registry
from db.sqlalchemy.metadata import metadata_obj
from core.models.food_category import FoodCategory


food_category = Table(
    "food_category",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("name", VARCHAR)
)

mapper_registry.map_imperatively(
    FoodCategory,
    food_category,
)
