from db import Database
from classes import Export

from aiogram import Bot, Dispatcher

db = Database('database.db')

bot = Bot('5768669556:AAGPgELc8AjQyZNiYLYeTmDFDMjGXOrxFhQ')
dp = Dispatcher(bot=bot)

db.add_vehicle('otomoto', Export(23, 'link', 'title', ['pic1'], 999, 'info', 'location'))
qwe = db.get_vehicle('otomoto', 123)
print(qwe)
