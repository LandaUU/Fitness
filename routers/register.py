from routers.core import dp

from routers.weight.router import weight_router
from routers.steps.router import steps_router


def register_routers():
    dp.include_router(weight_router)
    dp.include_router(steps_router)
