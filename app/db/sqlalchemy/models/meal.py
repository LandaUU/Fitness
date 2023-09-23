from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.meal import Meal


meal = Table(
    "meal",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("name", VARCHAR)
)

mapper_registry.map_imperatively(
    Meal,
    meal,
)
