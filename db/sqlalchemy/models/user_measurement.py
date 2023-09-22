from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import REAL, INTEGER, DATE
from sqlalchemy import Table
from db.sqlalchemy.mapper_registry import mapper_registry
from db.sqlalchemy.metadata import metadata_obj
from core.models.user_measurement import UserMeasurement


user_measurement = Table(
    "user_measurement",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("user_id", INTEGER),
    Column("pass_date", DATE),
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