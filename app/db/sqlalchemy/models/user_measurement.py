from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import REAL, INTEGER, DATE, BIGINT
from sqlalchemy import Table
from app.db.sqlalchemy.base import metadata_obj, mapper_registry
from app.core.models.user_measurement import UserMeasurement


user_measurement = Table(
    "user_measurement",
    metadata_obj,
    Column("user_id", BIGINT, ForeignKey("user.id"), primary_key=True),
    Column("pass_date", DATE, primary_key=True),
    Column("weight", REAL),
    Column("steps", INTEGER),
    Column("neck", REAL),
    Column("waist", REAL),
    Column("stomach", REAL),
    Column("hips", REAL),
    Column("hip", REAL),
    Column("shin", REAL),
    Column("chest", REAL),
    Column("biceps", REAL),
)

mapper_registry.map_imperatively(
    UserMeasurement,
    user_measurement,
)
