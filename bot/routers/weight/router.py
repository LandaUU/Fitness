from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from routers.weight.callback import WeightCallback
from routers.weight.states import WeightState
from routers.core import command_menu_handler
from tools import search_steps_number_in_text, UnexpectedAnswer, NegativeAnswer, NegativeNumber, delay

weight_router = Router(name="weight")


@weight_router.callback_query(WeightCallback.filter())
async def callback_router(query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    await state.set_state(WeightState.weight)
    await query.bot.send_message(chat_id=query.message.chat.id,
                                 text="Твой утренний вес? (Если не взвешивался так и напиши)")
    await query.answer()


@weight_router.message(Command("set_weight"))
async def command_router(message: Message, state: FSMContext):
    await state.set_state(WeightState.weight)
    await message.bot.send_message(chat_id=message.chat.id,
                                   text="Твой утренний вес? (Если не взвешивался так и напиши)")


@weight_router.message(WeightState.weight)
async def set_weight_router(message: Message, state: FSMContext):
    response_text = ""
    try:
        weight = await search_steps_number_in_text(message.text)
        await state.update_data(weight=weight)
        response_text = f"Спасибо, твой вес равен {weight} кг"
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=response_text)
        await delay(command_menu_handler(message), 1)
        await state.clear()
        return
    except NegativeNumber:
        response_text = 'Вес не может быть отрицательным, попробуй ещё раз'
    except NegativeAnswer:
        response_text = 'Спасибо, твой вес за сегодня не был измерен'
    except UnexpectedAnswer:
        response_text = 'Не понял тебя, попробуй ещё раз'

    await message.bot.send_message(chat_id=message.chat.id,
                                   text=response_text)
