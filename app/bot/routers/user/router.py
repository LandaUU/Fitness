from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.routers.user.callback import UserCreateCallback, UserCreateAction
from app.bot.routers.user.states import UserState, UserScenarioState
from app.bot.tools import search_steps_number_in_text, NegativeNumber, NegativeAnswer, UnexpectedAnswer
from app.bot.routers.fatsecret_reports.callback import FatSecretUserSyncCallback, FatSecretUserSyncAction
from app.core.models.user import User
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.user_repository import UserRepository

user_router = Router(name="user")


async def handle_user_answer(message: Message, state: FSMContext, attr_name,
                             negative_number_text,
                             negative_answer_text,
                             unexpected_answer_text,
                             answer_type: str = 'int') -> bool:
    try:
        if (answer_type == 'int'):
            answer = await search_steps_number_in_text(message.text)
        else:
            answer = message.text
        await state.update_data(**{attr_name: answer})
        return True
    except NegativeNumber:
        response_text = negative_number_text
    except NegativeAnswer:
        response_text = negative_answer_text
        await state.clear()
    except UnexpectedAnswer:
        response_text = unexpected_answer_text

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)
    return False


@user_router.callback_query(UserCreateCallback.filter(F.action == UserCreateAction.begin))
async def callback_router(query: CallbackQuery, callback_data: UserCreateCallback, state: FSMContext):
    if callback_data.action == UserCreateAction.begin:
        await query.bot.send_message(chat_id=query.message.chat.id,
                                     text='Давай начнем!')

    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Напиши своё ФИО:')
    await state.set_state(UserState.fio)
    await query.answer()


@user_router.message(UserState.fio)
async def fill_user_fio(message: Message, state: FSMContext):
    fio = message.text
    await state.update_data(fio=fio)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Укажи свой пол: М или Ж?')
    await state.set_state(UserState.gender)


@user_router.message(UserState.gender)
async def fill_user_gender(message: Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Сколько тебе полных лет?')
    await state.set_state(UserState.age)


@user_router.message(UserState.age)
async def fill_user_age(message: Message, state: FSMContext):
    if (await handle_user_answer(message, state, 'age',
                                 'Возраст не может быть отрицательным',
                                 'Ну нет, так нет',
                                 'Я ничего не понял, попробуй ещё раз')):
        response_text = "Твой рост?"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.height)


@user_router.message(UserState.height)
async def fill_user_height(message: Message, state: FSMContext):
    if (await handle_user_answer(message, state, 'height',
                                 'Рост не может быть отрицательным',
                                 'Ну нет, так нет',
                                 'Я ничего не понял, попробуй ещё раз')):
        response_text = """Оцени уровень своей физической активности, где:
- 1 низкая (большую часть дня провожу сидя)
- 2 средняя (2-3 тренировки в неделю + прогулки, в течении дня могу прогуляться)
- 3 высокая (4- 5 тренировок в неделю, много хожу пешком)"""
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.physical_level)


@user_router.message(UserState.physical_level)
async def fill_user_physical_level(message: Message, state: FSMContext):
    if (await handle_user_answer(message, state, 'physical_level',
                                 'Вариант не может быть отрицательным, попробуй ещё раз',
                                 'Ну нет, так нет',
                                 'Я ничего не понял, попробуй ещё раз')):
        response_text = """Есть ли у тебя диагностированные заболевания? (Перечисли все имеющиеся)
- Со стороны жкт (панкреатит и т.д)
- Со стороны гормональной системы (инсулинорезистентность, дефицит половых гормонов, гипотиреоз и т.д)
- Со стороны сердечно-сосудистой системы (гипертония, аритмия и т.д)
- Со стороны выделительной системы
- Со стороны опорно-двигательного аппарата (артриты, грыжи и т.д)"""
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.sickness)


@user_router.message(UserState.sickness)
async def fill_user_sickness(message: Message, state: FSMContext):
    if (await handle_user_answer(message, state, 'sickness',
                                 'Ну, негативное число здесь невозможно получить',
                                 'Ну нет, так нет',
                                 'Я ничего не понял, попробуй ещё раз', 'str')):
        response_text = """Имеется ли у тебя опыт похудения (в ответ напиши номер подходящего варианта)
1. Да, есть большой опыт похудений и откатов
2. Есть успешный опыт похудения и удержания результата
3. Ранее не худел(а)"""
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.losing_weight_level)


@user_router.message(UserState.losing_weight_level)
async def fill_user_losing_weight_level(message: Message, state: FSMContext):
    if (await handle_user_answer(message, state, 'losing_weight_level',
                                 'Вариант не может быть отрицательным, попробуй ещё раз',
                                 'Ну нет, так нет',
                                 'Я ничего не понял, попробуй ещё раз')):
        response_text = """Худел(а) ли ты в последние пол года
1. Да, но все набрал(а) обратно
2. Да худел(а) и удерживаю результат
3. Нет не худел(а)"""
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.losing_weight_in_half_year_level)


@user_router.message(UserState.losing_weight_in_half_year_level)
async def fill_user_losing_weight_in_half_year_level(message: Message, state: FSMContext):
    if (await handle_user_answer(message, state, 'losing_weight_in_half_year_level',
                                 'Вариант не может быть отрицательным, попробуй ещё раз',
                                 'Ну нет, так нет',
                                 'Я ничего не понял, попробуй ещё раз')):
        await message.bot.send_message(chat_id=message.chat.id,
                                       text='Хорошо!')
        await state.set_state(UserScenarioState.check)
        await message.bot.send_message(chat_id=message.chat.id,
                                       text='Давай теперь проверим твои данные:')
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=str(await state.get_data()))
        response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Да",
                                  callback_data=UserCreateCallback(action=UserCreateAction.save).pack())],
            [InlineKeyboardButton(text="Нет",
                                  callback_data=UserCreateCallback(action=UserCreateAction.begin).pack())]])
        await message.bot.send_message(chat_id=message.chat.id,
                                       text='Всё верно?',
                                       reply_markup=response_keyboard)


@user_router.callback_query(UserCreateCallback.filter(F.action == UserCreateAction.save))
async def save_user_report(query: CallbackQuery, callback_data: UserCreateCallback, state: FSMContext):
    user_dict = await state.get_data()

    new_user = User(**user_dict)

    new_user.telegram_id = query.from_user.id
    new_user.telegram_username = query.from_user.username

    repository = UserRepository(session=async_session)

    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Привязать трекер еды",
                              callback_data=FatSecretUserSyncCallback(action=FatSecretUserSyncAction.begin).pack())]])

    await repository.save(new_user)
    await state.clear()
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Сохранено!')
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Давай перейдем к следующему этапу и синхронизируем фатсикрет с ботом',
                                 reply_markup=response_keyboard)
