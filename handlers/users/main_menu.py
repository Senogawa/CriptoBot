from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline import menu_board, back_board, start_board
from middlewares.get_thresholds_info import get_thresholds



async def start(message: types.Message):
    await message.answer("Бот создан для торговли на бирже binance\nСпотовая торговля происходит на паре USDT/DAI", reply_markup = start_board)


async def main_menu(call: types.CallbackQuery):
    thresholds_meta = get_thresholds()
    await call.message.edit_text(f"""
    Состояние ордера - 
Текущий курс - 
Последняя покупка - 
Последняя продажа - 
===================
Порог покупки - {thresholds_meta['threshold_buy']}
Порог продажи - {thresholds_meta['threshold_sell']}
    """, reply_markup = menu_board)
    del thresholds_meta



def register_all_main_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands = "start")
    dp.register_callback_query_handler(main_menu, Text(equals = "start"))