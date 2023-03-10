from create_bot import bot, db

from aiogram.types import CallbackQuery, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


async def help_with_callback(callback: CallbackQuery):
    vehicle = db.get_vehicle(site_name=callback.data.split(' ')[1], vehicle_id=callback.data.split(' ')[2])

    await bot.send_photo(chat_id=856367900,
                         photo=vehicle.picture,
                         caption=f'{callback.from_user.full_name} заинтересовался предложением:\n'
                                 f'<a href="{vehicle.link}"><b>{vehicle.title}</b></a>\n\n'
                                 f'<b>Цена (с наценкой 15.000$):</b> {vehicle.price} $\n'
                                 f'<b>Локация:</b> {vehicle.location}\n'
                                 f"<b>Описание:</b> {vehicle.info}\n\n",
                         parse_mode=ParseMode.HTML,
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                             [InlineKeyboardButton(url=callback.from_user.url, text=f'Связаться с {callback.from_user.full_name}')]
                         ]))

    # await bot.send_photo(chat_id=1331812370,
    #                      photo=vehicle.picture,
    #                      caption=f'{callback.from_user.full_name} заинтересовался предложением:\n'
    #                              f'<a href="{vehicle.link}"><b>{vehicle.title}</b></a>\n\n'
    #                              f'<b>Цена (с наценкой 15.000$):</b> {vehicle.price} $\n'
    #                              f'<b>Локация:</b> {vehicle.location}\n'
    #                              f"<b>Информация:</b> {vehicle.info}\n\n",
    #                      parse_mode=ParseMode.HTML,
    #                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
    #                          [InlineKeyboardButton(url=callback.from_user.url, text=f'Связаться с {callback.from_user.full_name}')]
    #                      ]))

    await callback.answer(text='Спасибо. Заявка принята. В ближайшее время с Вами свяжется наш менеджер.', show_alert=True)
