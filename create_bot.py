from db import Database

from aiogram import Bot, Dispatcher

db = Database('database.db')


bot = Bot('5768669556:AAGPgELc8AjQyZNiYLYeTmDFDMjGXOrxFhQ')
dp = Dispatcher(bot=bot)
