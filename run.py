import asyncio
import os
import logging

from aiogram import Bot, Dispatcher

from app.client import client
from app.database.models import init_models


async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(client)
    bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(startup)
    dp.startup.register(shutdown)
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    await init_models()
    logging.info('Bot started up...')


async def shutdown(dispatcher: Dispatcher):
    logging.info('Bot shutting down')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Bot stopped')