import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from tg_data.data import config
# from handlers import router
from tg_data.handlers.client import client_handler


async def main():
    bot = Bot(token=config.telegram_bot, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())



    dp.include_routers(client_handler.router)





    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())