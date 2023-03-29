import os

from db import Database

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode

db = Database('database.db')


bot = Bot(os.getenv('VEHICLE_SELLER_API_KEY'), parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)
