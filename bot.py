from gettext import dpgettext
from multiprocessing.managers import DictProxy
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from loader import bot_mn
import handlers


dp = Dispatcher(bot_mn, storage = MemoryStorage())

handlers.register_all_users_handlers(dp)


async def bot_start_pooling():
    try:
        await dp.start_polling()
    finally:
        dp.storage.close()




if __name__ == "__main__":
    asyncio.run(bot_start_pooling())