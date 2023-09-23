from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, REAL, INTEGER, DATE, BIGINT
from sqlalchemy import Table
from app.core.models.user import User
from app.db.sqlalchemy.base import metadata_obj, mapper_registry

user = Table(
    "user",
    metadata_obj,
    Column("id", BIGINT, primary_key=True),
    Column("fio", VARCHAR),
    Column("lastname", VARCHAR),
    Column("middlename", VARCHAR),
    Column("firstname", VARCHAR),
    Column("height", REAL),
    Column("age", INTEGER),
    Column("birthday", DATE),
    Column("gender", VARCHAR),
    Column("telegram_id", BIGINT),
    Column("telegram_username", VARCHAR),
    Column("pay_date", DATE),
    Column("next_report_date", DATE),
    Column("exit_date", DATE),
    Column("oauth_token", VARCHAR),
    Column("oauth_secret", VARCHAR),
    Column("oauth_date", DATE),
)

mapper_registry.map_imperatively(
    User,
    user,
)
