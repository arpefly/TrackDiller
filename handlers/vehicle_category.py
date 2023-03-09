from aiogram.types import CallbackQuery

from keyboards.inline import vehicle_brand


async def vehicle_category_callback(callback: CallbackQuery):
    await callback.message.answer('Марка авто', reply_markup=vehicle_brand)
    await callback.answer()
    await callback.message.delete()
