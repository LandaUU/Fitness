from routers.core import dp

from routers.weight.router import weight_router


def register_routers():
    dp.include_router(weight_router)
