from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from bot.routers.core import command_menu_handler
from bot.routers.steps.callback import StepsCallback
from bot.routers.steps.state import StepsState
from bot.tools import search_steps_number_in_text, UnexpectedAnswer, NegativeAnswer, NegativeNumber, delay

steps_router = Router(name="steps")


@steps_router.callback_query(StepsCallback.filter())
async def callback_router(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await state.set_state(StepsState.steps)
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text="Сколько шагов сегодня прошел (Если не следил так и напиши)")
    await query.answer()


@steps_router.message(Command("set_steps"))
async def command_router(message: Message, state: FSMContext):
    await state.set_state(StepsState.steps)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text="Сколько шагов сегодня прошел (Если не следил так и напиши)")


@steps_router.message(StepsState.steps)
async def set_steps_router(message: Message, state: FSMContext):
    response_text = ""
    try:
        steps = int(await search_steps_number_in_text(message.text))
        await state.update_data(steps=steps)
        response_text = f"Спасибо, ты прошёл за сегодня {steps} шагов"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await delay(command_menu_handler(message), 1)
        await state.clear()
        return
    except NegativeNumber:
        response_text = 'Кол-во шагов не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Спасибо, твои шаги за сегодня мы не записали'
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)
