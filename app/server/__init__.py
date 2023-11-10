from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from .routers.user import user_routes
from .middleware.telegram import TelegramMiddleware

app = Starlette(debug=True, routes=user_routes, middleware=[Middleware(
    TelegramMiddleware), Middleware(CORSMiddleware, allow_origins=['*'])])
