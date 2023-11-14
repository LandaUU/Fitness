from starlette.responses import Response
from starlette.requests import Request
from app.db.sqlalchemy.repositories.repository import EntityRepository
from app.core.models.food_diary import FoodDiary
from app.db.sqlalchemy.base import async_session
import json


async def get_food_diary(request: Request):
    import app.db.sqlalchemy.models

    repository = EntityRepository(async_session, FoodDiary)

    user_id = request.query_params.get('user_id')

    user_diary: FoodDiary = await repository.get(lambda d: d.user_id == user_id)

    if user_diary is None:
        return Response(status_code=404)

    return Response(content=json.dumps(user_diary), status_code=200)
