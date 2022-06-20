from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
import json
import aioschedule

from keyboards.inline import back_board, set_menu_s_board, set_menu_b_board, menu_board
from states.state import BotStates
from middlewares.get_json_info import get_thresholds, set_thresholds
from middlewares.scheduler.aiorefresh import schedule_stats
from loader import bot_mn


async def threshold_s(call: types.CallbackQuery, state: FSMContext):
    aioschedule.clear(f"{call.message.from_user.id}")
    await call.message.edit_text("Введите порог продажи", reply_markup = back_board)
    await BotStates.sell_threshold_state.set()
    await state.update_data(call_message=call.message.message_id)


async def threshold_b(call: types.CallbackQuery, state: FSMContext):
    aioschedule.clear(f"{call.message.from_user.id}")
    await call.message.edit_text("Введите порог покупки", reply_markup = back_board)
    await BotStates.buy_threshold_state.set()
    await state.update_data(call_message=call.message.message_id)


async def threshold_s_state(message: types.Message, state: FSMContext):
    call_message_id = await state.get_data()
    try:
        thresholds_data = get_thresholds()
        thresholds_data["threshold_sell"] = float(message.text)
        set_thresholds(thresholds_data)

    except ValueError:
        await bot_mn.delete_message(message.chat.id, message.message_id)
        try:
            await bot_mn.edit_message_text("Это должно быть число", message.chat.id, call_message_id["call_message"], reply_markup = back_board)
        except MessageNotModified:
            print("not modify")
        return

    
    await bot_mn.delete_message(message.chat.id, message.message_id)

    del thresholds_data

    await bot_mn.edit_message_text(f"Данные изменены\nТекущий порог продажи - {float(message.text)}", message.chat.id, call_message_id["call_message"], reply_markup = set_menu_s_board)
    await state.finish()



async def threshold_b_state(message: types.Message, state: FSMContext):
    call_message_id = await state.get_data()
    try:
        thresholds_data = get_thresholds()
        thresholds_data["threshold_buy"] = float(message.text)
        set_thresholds(thresholds_data)

    except ValueError:
        await bot_mn.delete_message(message.chat.id, message.message_id)
        try:
            await bot_mn.edit_message_text("Это должно быть число", message.chat.id, call_message_id["call_message"], reply_markup = back_board)
        except MessageNotModified:
            print("not modify")
        return

    await bot_mn.delete_message(message.chat.id, message.message_id)

    del thresholds_data

    await bot_mn.edit_message_text(f"Данные изменены\nТекущий порог покупки - {float(message.text)}", message.chat.id, call_message_id["call_message"], reply_markup = set_menu_b_board)
    await state.finish()


async def newtry_sell(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новый порог продажи", reply_markup = back_board)
    await BotStates.sell_threshold_state.set()
    await state.update_data(call_message=call.message.message_id)


async def newtry_buy(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новый порог покупки", reply_markup = back_board)
    await BotStates.buy_threshold_state.set()
    await state.update_data(call_message=call.message.message_id)


async def set_main_menu(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await schedule_stats(call)


def register_all_thresholds_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(threshold_s, Text(equals = "sell_threshold"))
    dp.register_callback_query_handler(threshold_b, Text(equals = "buy_threshold"))
    dp.register_message_handler(threshold_s_state, state = BotStates.sell_threshold_state)
    dp.register_message_handler(threshold_b_state, state = BotStates.buy_threshold_state)
    dp.register_callback_query_handler(set_main_menu, Text(equals = "main_menu"))
    dp.register_callback_query_handler(set_main_menu, Text(equals = "back"), state = BotStates.sell_threshold_state)
    dp.register_callback_query_handler(set_main_menu, Text(equals = "back"), state = BotStates.buy_threshold_state)
    dp.register_callback_query_handler(newtry_sell, Text(equals = "newtry_sell"))
    dp.register_callback_query_handler(newtry_buy, Text(equals = "newtry_buy"))