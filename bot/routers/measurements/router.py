from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.callback_data import CallbackData
from bot.routers.core import command_menu_handler
from bot.tools import search_steps_number_in_text, UnexpectedAnswer, NegativeAnswer, NegativeNumber, delay
from bot.routers.measurements.callback import MeasureCallback
from bot.routers.measurements.state import MeasureState

measure_router = Router(name="measure")


@measure_router.callback_query(MeasureCallback.filter())
async def callback_router(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await state.set_state(MeasureState.Neck)
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text="Давай начнем. Напиши охват шеи в см:")
    await query.answer()


@measure_router.message(Command("set_measurement"))
async def command_router(message: Message, state: FSMContext):
    await state.set_state(MeasureState.Neck)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text="Давай начнем. Напиши охват шеи в см:")


@measure_router.message(MeasureState.Neck)
async def set_neck_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        neck_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Neck=neck_size)
        await state.set_state(MeasureState.Waist)
        response_text = f"Твой охват шеи равен {neck_size} см, едем дальше. Напиши охват талии в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Waist)
async def set_waist_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        waist_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Waist=waist_size)
        await state.set_state(MeasureState.Stomach)
        response_text = f"Твой охват талии равен {waist_size} см, едем дальше. Напиши охват живота в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Stomach)
async def set_stomach_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        stomach_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Stomach=stomach_size)
        await state.set_state(MeasureState.Hips)
        response_text = f"Твой охват живота равен {stomach_size} см, едем дальше. Напиши охват бедер в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Hips)
async def set_hips_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        hips_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Stomach=hips_size)
        await state.set_state(MeasureState.Hip)
        response_text = f"Твой охват бедер равен {hips_size} см, едем дальше. Напиши охват бедра в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Hip)
async def set_hip_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        hip_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Hip=hip_size)
        await state.set_state(MeasureState.Shin)
        response_text = f"Твой охват бедра равен {hip_size} см, едем дальше. Напиши охват голени в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Shin)
async def set_shin_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        shin_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Shin=shin_size)
        await state.set_state(MeasureState.Chest)
        response_text = f"Твой охват голени равен {shin_size} см, едем дальше. Напиши охват груди в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Chest)
async def set_chest_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        chest_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Chest=chest_size)
        await state.set_state(MeasureState.Biceps)
        response_text = f"Твой охват груди равен {chest_size} см, едем дальше. Напиши охват бицепса в см:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)


@measure_router.message(MeasureState.Biceps)
async def set_biceps_size(message: Message, state: FSMContext):
    response_text = ""
    try:
        biceps_size = int(await search_steps_number_in_text(message.text))
        await state.update_data(Biceps=biceps_size)
        await state.set_state(MeasureState.Hips)
        response_text = f"Твой охват бицепса равен {biceps_size} см, смотри что получилось:"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        measure_template_text = 'Шея - {}\nТалия - {}\n' + \
            'Живот - {}\nБедра - {}\nБедро - {}\nГолень - {}\nГрудь - {}\nБицепс - {}'
        values = list((await state.get_data()).values()) + [biceps_size]
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=measure_template_text.format(*values))
        await delay(command_menu_handler(message), 1)
        await state.clear()
        return
    except NegativeNumber:
        response_text = 'Охват не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Ну ты это, скинь замеры позже тогда)'
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await state.clear()
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)
