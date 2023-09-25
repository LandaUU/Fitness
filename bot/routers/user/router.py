from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from bot.routers.user.callback import UserCreateCallback
from bot.routers.user.states import UserCreateState
from bot.tools import search_steps_number_in_text, NegativeNumber, NegativeAnswer, UnexpectedAnswer
from app.core.models.user import User
from app.db.sqlalchemy.models.user import user
from app.db.sqlalchemy.base import async_session
from app.db.sqlalchemy.repositories.user_repository import UserRepository

user_router = Router(name="user")


@user_router.callback_query(UserCreateCallback.filter(F.final == False))
async def callback_router(query: CallbackQuery, callback_data: UserCreateCallback, state: FSMContext):
    if callback_data.is_first_report:
        await query.bot.send_message(chat_id=query.message.chat.id,
                                     text='Давай начнем!')

    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Напиши своё ФИО:')
    await state.set_state(UserCreateState.fio)
    await query.answer()


@user_router.message(UserCreateState.fio)
async def fill_user_fio(message: Message, state: FSMContext):
    fio = message.text
    await state.update_data(fio=fio)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Сколько тебе полных лет?')
    await state.set_state(UserCreateState.age)


@user_router.message(UserCreateState.age)
async def fill_user_age(message: Message, state: FSMContext):
    try:
        age = await search_steps_number_in_text(message.text)
        await state.update_data(age=age)
        response_text = f"Твой рост?"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserCreateState.height)
        return
    except NegativeNumber:
        response_text = 'Возраст не может быть отрицательным, попробуй ещё раз'
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@user_router.message(UserCreateState.height)
async def fill_user_height(message: Message, state: FSMContext):
    try:
        height = await search_steps_number_in_text(message.text)
        await state.update_data(height=height)
        response_text = f"Давай теперь напиши свой пол, М или Ж?"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.set_state(UserCreateState.gender)
        return
    except NegativeNumber:
        response_text = 'Вес не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Спасибо, твой вес за сегодня не был измерен'
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@user_router.message(UserCreateState.gender)
async def fill_user_gender(message: Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Хорошо!')
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Давай теперь проверим твои данные:')
    await state.set_state(UserCreateState.data_report)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text=str(await state.get_data()))


@user_router.message(UserCreateState.data_report)
async def check_user_report(message: Message, state: FSMContext):
    response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Да",
                              callback_data=UserCreateCallback(is_first_report=True, final=True).pack())],
        [InlineKeyboardButton(text="Нет",
                              callback_data=UserCreateCallback(is_first_report=True, final=False).pack())]])
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Всё верно?',
                                   reply_markup=response_keyboard)


@user_router.callback_query(UserCreateCallback.filter(F.final == True))
async def save_user_report(query: CallbackQuery, callback_data: UserCreateCallback, state: FSMContext):
    user_dict = await state.get_data()

    new_user = User(**user_dict)

    repository = UserRepository(session=async_session)

    await repository.create_user(new_user)

    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text='Сохранено!')
