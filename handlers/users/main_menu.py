from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline import menu_board, back_board, start_board
from middlewares.get_json_info import get_thresholds
from middlewares.scheduler.aiorefresh import schedule_stats



async def start(message: types.Message):
    await message.answer("Бот создан для торговли на бирже binance\nСпотовая торговля происходит на паре USDT/DAI", reply_markup = start_board)

async def main_menu(call: types.CallbackQuery):
    await schedule_stats(call)



def register_all_main_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands = "start")
    dp.register_callback_query_handler(main_menu, Text(equals = "start"))