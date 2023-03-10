from broadcster import broadcast

from aiogram.types import Message


async def start_command(message: Message):
    await broadcast()
