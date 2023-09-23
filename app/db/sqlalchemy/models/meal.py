from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, BIGINT
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.meal import Meal


meal = Table(
    "meal",
    metadata_obj,
    Column("id", BIGINT, primary_key=True),
    Column("name", VARCHAR)
)

mapper_registry.map_imperatively(
    Meal,
    meal,
)
