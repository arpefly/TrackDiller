from create_bot import bot, db

from aiogram.types import CallbackQuery


async def help_with_callback(callback: CallbackQuery):


    await bot.send_message(chat_id=856367900, text=f'')

    await callback.answer(text='Спасибо. Заявка принята. В ближайшее время с Вами свяжется наш менеджер.', show_alert=True)
