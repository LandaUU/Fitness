from starlette.middleware.base import BaseHTTPMiddleware


class TelegramMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(await request.body())
        print(request.query_params)
        response = await call_next(request)
        return response
