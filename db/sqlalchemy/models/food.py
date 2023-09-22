from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy import Table
from db.sqlalchemy.mapper_registry import mapper_registry
from db.sqlalchemy.metadata import metadata_obj
from core.models.food import Food


food = Table(
    "food",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("name", VARCHAR),
    Column("category_id", INTEGER),
)

mapper_registry.map_imperatively(
    Food,
    food,
)
