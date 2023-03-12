import asyncio

from create_bot import bot, db
from utils.config import Admin, Customer

from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message


async def help_with_callback(callback: CallbackQuery):
    vehicle = db.get_vehicle(site_name=callback.data.split(' ')[1], vehicle_id=callback.data.split(' ')[2])

    try:
        for user in [Admin]:  # , Customer]:
            await bot.send_photo(chat_id=user,
                                 photo=vehicle.photos.split(';')[0],
                                 caption=f'{callback.from_user.full_name} заинтересовался предложением:\n'
                                         f'<a href="{vehicle.link}"><b>{vehicle.title}</b></a>\n\n'
                                         f'<b>Цена (с наценкой 15.000$):</b> {vehicle.price} $\n'
                                         f'<b>Год выпуска:</b> {vehicle.year}\n'
                                         f'<b>Коробка передач:</b> {vehicle.transmission}\n'
                                         f'<b>Локация:</b> {vehicle.location}\n'
                                         f'<a href="{callback.message.url}"><b>Ссылка на пост в канале</b></a>',
                                 reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                     [InlineKeyboardButton(url=callback.from_user.url, text=f'Связаться с {callback.from_user.full_name}')]
                                 ]))

        await callback.answer(text='Спасибо. Заявка принята. В ближайшее время с Вами свяжется наш менеджер.', show_alert=True)
    except Exception as ex:
        print(ex)
        await asyncio.sleep(5)
