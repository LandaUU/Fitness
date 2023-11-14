from starlette.routing import Route
from .get import get_user

user_routes = [
    Route("/users/get", endpoint=get_user),
]
