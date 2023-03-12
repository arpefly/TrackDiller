from db import Database

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode

db = Database('database.db')


bot = Bot('5768669556:AAGPgELc8AjQyZNiYLYeTmDFDMjGXOrxFhQ', parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)
