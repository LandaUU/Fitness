from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy import Table
from db.sqlalchemy.base import metadata_obj, mapper_registry
from core.models.food import Food


food = Table(
    "food",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("name", VARCHAR),
    Column("category_id", INTEGER, ForeignKey("food_category.id")),
)

mapper_registry.map_imperatively(
    Food,
    food,
)
