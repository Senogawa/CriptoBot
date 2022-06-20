import aioschedule
import asyncio
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified
from binance import AsyncClient

from binance_logic.binance_get_info import get_price, get_orders_sandb
from keyboards.inline import menu_board
from middlewares.get_json_info import get_thresholds
from loader import binance_meta

async def reset_message(call: CallbackQuery):
    cm_client = await AsyncClient.create(binance_meta.key, binance_meta.secret)
    thresholds_meta = get_thresholds()
    orders_stats = await get_orders_sandb(cm_client)
    valute_price = await get_price(cm_client)
    if valute_price == None: 
        return

    try:
        await call.message.edit_text(f"""
        Состояние ордера - {orders_stats["new_order"]["side"]} {orders_stats["new_order"]["price"]}
Текущий курс - {valute_price}
Последняя покупка - {orders_stats["last_buy"]["price"]}
Последняя продажа - {orders_stats["last_sell"]["price"]}
===================
Порог покупки - {thresholds_meta['threshold_buy']}
Порог продажи - {thresholds_meta['threshold_sell']}
        """, reply_markup = menu_board)
    except MessageNotModified:
        print("not modify")
    finally:
        del thresholds_meta

async def schedule_stats(call: CallbackQuery):
    aioschedule.every(0.5).seconds.do(reset_message, call).tag(f"{call.message.from_user.id}")
    while True:
        if not aioschedule.jobs:
            break
        await aioschedule.run_pending()
        await asyncio.sleep(0)