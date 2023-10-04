from datetime import datetime
from app.core.models.food import Food

from app.core.models.food_diary import FoodDiary
from app.core.models.user import User
from app.modules.fatsecret.client import fatsecret_client
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.food_diary_repository import FoodDiaryRepository
from app.db.sqlalchemy.repositories.repository import EntityRepository
from app.core.models.meal import Meal


async def save_food(entry: dict, food_detail: dict) -> Food:
    repository = EntityRepository(session=async_session, entity_type=Food)
    food = await repository.get(lambda f: f.id == int(entry['food_id']))

    if not food:
        food = Food(id=int(entry['food_id']), name=food_detail['food_name'], category_id=None)
        await repository.save(food)

    return food


async def save_meal(entry: dict) -> Meal:
    meal_repository = EntityRepository(session=async_session, entity_type=Meal)
    meal = await meal_repository.get(lambda m: m.name == entry['meal'])

    if not meal:
        meal = Meal(name=entry['meal'])
        await meal_repository.save(meal)

    return meal


async def save_user_report(user: User, diary_date: datetime) -> None:
    entries = fatsecret_client.get_user_report((user.oauth_token, user.oauth_secret), diary_date=diary_date)
    diary = []
    for entry in entries:
        food_details = fatsecret_client.get_food_details(entry['food_id'])
        if isinstance(food_details['servings']['serving'], list):
            serving = next(filter(lambda s: s['serving_id'] == entry['serving_id'], food_details['servings']['serving']))
        else:
            serving = food_details['servings']['serving']
        if serving['measurement_description'] != 'g':
            food_grams = float(serving['metric_serving_amount']) * float(entry['number_of_units'])
        else:
            food_grams = float(entry['number_of_units'])

        meal = await save_meal(entry)

        food = await save_food(entry, food_details)

        diary.append(FoodDiary(
            food_id=food.id,
            user_id=user.id,
            meal_id=meal.id,
            diary_date=diary_date.date(),
            amount=food_grams,
            metric_type=1,
            calories=float(entry['calories']),
            protein=float(entry['protein']),
            carbohydrate=float(entry['carbohydrate']),
            fat=float(entry['fat'])
        ))

    diary_repository = FoodDiaryRepository(session=async_session)
    await diary_repository.save_all(diary)
    # for d in diary:
    #     await diary_repository.save(d)
