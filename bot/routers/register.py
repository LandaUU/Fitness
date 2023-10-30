from bot.routers.core import dp

from bot.routers.weight.router import weight_router
from bot.routers.steps.router import steps_router
from bot.routers.measurements.router import measure_router
from bot.routers.fatsecret_reports.router import fatsecret_router
from bot.routers.user.router import user_router
from bot.routers.reports.router import reports
from bot.routers.admin.router import admin_router


def register_routers():
    dp.include_router(weight_router)
    dp.include_router(steps_router)
    dp.include_router(measure_router)
    dp.include_router(fatsecret_router)
    dp.include_router(user_router)
    dp.include_router(reports)
    dp.include_router(admin_router)
