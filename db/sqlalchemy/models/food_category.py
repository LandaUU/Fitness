from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, REAL, INTEGER, DATE
from sqlalchemy import Table
from db.sqlalchemy.mapper_registry import mapper_registry
from db.sqlalchemy.metadata import metadata_obj
from core.models.food_category import FoodCategory


food_category = Table(
    "food_category",
    metadata_obj,
    Column("id", INTEGER, primary_key=True),
    Column("name", VARCHAR),
    Column("lastname", VARCHAR),
    Column("middlename", VARCHAR),
    Column("firstname", VARCHAR),
    Column("height", REAL),
    Column("age", INTEGER),
    Column("birthday", DATE),
    Column("gender", VARCHAR),
    Column("pay_date", DATE),
    Column("next_report_date", DATE),
    Column("exit_date", DATE),
    Column("oauth_token", VARCHAR),
    Column("oauth_secret", VARCHAR),
    Column("oauth_date", DATE),
)

mapper_registry.map_imperatively(
    FoodCategory,
    food_category,
)
