from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy import Table
from db.sqlalchemy.mapper_registry import mapper_registry
from db.sqlalchemy.metadata import metadata_obj
from core.models.metric_type import MetricType


metric_type = Table(
    "metric_type",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("type", VARCHAR),
    Column("description", VARCHAR)
)

mapper_registry.map_imperatively(
    MetricType,
    mapper_registry,
)
