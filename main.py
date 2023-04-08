import asyncio
import tracemalloc

import aioschedule
from aiogram import executor

import handlers
from broadcster import broadcast
from create_bot import dp


async def scheduler():
    """
    Планировщик рассылки
    """

    aioschedule.every(1).hour.at(':00').do(lambda: asyncio.create_task(broadcast()))

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(10)


async def on_startup(_):
    handlers.setup(dp)
    asyncio.create_task(scheduler())
    print('bot is online')

    await broadcast()


async def on_shutdown(_):
    aioschedule.clear()


if __name__ == '__main__':
    tracemalloc.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
