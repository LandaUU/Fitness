from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from bot.routers.user.callback import UserCreateCallback, UserCreateAction
from bot.routers.user.states import UserState, UserScenarioState
from bot.tools import search_steps_number_in_text, NegativeNumber, NegativeAnswer, UnexpectedAnswer
from bot.routers.fatsecret_reports.callback import FatSecretUserSyncCallback, FatSecretUserSyncAction
from app.core.models.user import User
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.user_repository import UserRepository

user_router = Router(name="user")


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
                                   text='Сколько тебе полных лет?')
    await state.set_state(UserState.age)


@user_router.message(UserState.age)
async def fill_user_age(message: Message, state: FSMContext):
    try:
        age = await search_steps_number_in_text(message.text)
        await state.update_data(age=age)
        response_text = f"Твой рост?"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.height)
        return
    except NegativeNumber:
        response_text = 'Возраст не может быть отрицательным, попробуй ещё раз'
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@user_router.message(UserState.height)
async def fill_user_height(message: Message, state: FSMContext):
    try:
        height = await search_steps_number_in_text(message.text)
        await state.update_data(height=height)
        response_text = f"Давай теперь напиши свой пол, М или Ж?"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserState.gender)
        return
    except NegativeNumber:
        response_text = 'Вес не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Спасибо, твой вес за сегодня не был измерен'
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@user_router.message(UserState.gender)
async def fill_user_gender(message: Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
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
