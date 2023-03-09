from aiogram.types import CallbackQuery

from keyboards.inline import vehicle_category


async def vehicle_condition_callback(callback: CallbackQuery):
    await callback.message.answer('Категория авто', reply_markup=vehicle_category)
    await callback.answer()
    await callback.message.delete()
