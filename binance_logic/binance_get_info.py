from xml.dom.pulldom import parseString
from binance import AsyncClient
import aioschedule
import asyncio

from loader import binance_meta
from middlewares.get_json_info import get_binance_orders_json, set_binance_orders_json

async def get_price(cm_client: AsyncClient):
    valute_price = await cm_client.get_ticker(**{"symbol":binance_meta.symbol})
    valute_price = valute_price["lastPrice"]
    await asyncio.sleep(0.2)
    if not aioschedule.jobs:
        await cm_client.close_connection()
        return None
    await cm_client.close_connection()
    return valute_price

async def get_orders_sandb(cm_client: AsyncClient) -> dict:
    cm_client = await AsyncClient.create(binance_meta.key, binance_meta.secret)
    api_orders = await cm_client.get_all_orders(**{"symbol":binance_meta.symbol, "limit":5})

    file_orders = get_binance_orders_json()
    await cm_client.close_connection()
    have_new = False
    for order in api_orders:
        if order["side"] == "BUY" and order["status"] == "FILLED":
            file_orders["last_buy"]["orderid"] = order["orderId"]
            file_orders["last_buy"]["price"] = order["price"]

        elif order["side"] == "SELL" and order["status"] == "FILLED":
            file_orders["last_sell"]["orderid"] = order["orderId"]
            file_orders["last_sell"]["price"] = order["price"]

        elif order["status"] == "NEW":
            file_orders["new_order"]["side"] = order["side"]
            file_orders["new_order"]["price"] = order["price"]
            have_new = True
    if have_new == 0:
        file_orders["new_order"]["side"] = "no orders"
        file_orders["new_order"]["price"] = ""



    set_binance_orders_json(file_orders)
    return file_orders
        

# if __name__ == "__main__":
#     asyncio.run(test())