from starlette.responses import Response
from app.db.sqlalchemy.repositories.repository import EntityRepository
from app.core.models.user import User
from app.db.sqlalchemy.base import async_session
import json


async def get_user(request):
    import app.db.sqlalchemy.models
    repository = EntityRepository(async_session, User)

    users: list[User, None] = await repository.all()
    print(users)
    return Response(status_code=200,
                    content=json.dumps(list(map(lambda user: {"id": user.id, "name": user.fio}, users))))
