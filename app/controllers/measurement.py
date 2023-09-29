from datetime import datetime

from app.core.models.user import User
from app.core.models.user_measurement import UserMeasurement
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.measurement_repository import MeasurementRepository
from app.db.sqlalchemy.repositories.user_repository import UserRepository


async def _get_user(telegram_id: int) -> User:
    user_rep = UserRepository(session=async_session)
    return await user_rep.get_user(lambda u: u.telegram_id == telegram_id)


async def save_measurements(telegram_id: int, **kwargs):
    user = await _get_user(telegram_id)

    measurements_rep = MeasurementRepository(session=async_session)
    measurement = await measurements_rep.get_measurement(
        lambda m: m.user_id == user.id and m.pass_date == datetime.now().date()
    )

    if not measurement:
        measurement = UserMeasurement(user_id=user.id, pass_date=datetime.now().date(), **kwargs)
    else:
        for key, value in kwargs.items():
            setattr(measurement, key.lower(), value)

    await measurements_rep.save(measurement)
