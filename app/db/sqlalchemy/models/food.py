from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, BIGINT
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.food import Food


food = Table(
    "food",
    metadata_obj,
    Column("id", BIGINT, primary_key=True),
    Column("name", VARCHAR),
    Column("category_id", BIGINT, ForeignKey("food_category.id")),
)

mapper_registry.map_imperatively(
    Food,
    food,
)
