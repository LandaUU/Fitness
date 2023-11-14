from starlette.routing import Route
from .get_food_diary import get_food_diary

diary_routes = [
    Route("/diary/food", endpoint=get_food_diary),
]
