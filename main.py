import asyncio
import aioschedule

from aiogram import executor

import handlers
from create_bot import dp
from broadcster import broadcast


async def scheduler():
    """
    Планировщик рассылки уведомлений
    """

    aioschedule.every(1).hour.at(':00').do(broadcast)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    handlers.setup(dp)
    #  asyncio.create_task(scheduler())
    print('bot is online')

    await broadcast()


async def on_shutdown(_):
    aioschedule.clear()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
