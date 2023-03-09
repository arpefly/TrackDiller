from aiogram.types import Message

from keyboards.inline import vehicle_condition


async def configure_search_button(message: Message):
    await message.answer('Настройка поиска автомобилей')
    await message.answer('Выберите состояние автомобиля:', reply_markup=vehicle_condition)
