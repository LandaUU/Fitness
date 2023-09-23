from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.metric_type import MetricType


metric_type = Table(
    "metric_type",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("type", VARCHAR),
    Column("description", VARCHAR)
)

mapper_registry.map_imperatively(
    MetricType,
    metric_type,
)
