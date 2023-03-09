from aiogram.types import ParseMode
from aiogram.types import InputMediaPhoto
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import bot
from otomoto import otomoto_trackors
from classes import Export


async def broadcast():
    vehicles = otomoto_trackors()

    with open('broadcster/parsed_otomoto.txt', 'r+') as file:
        parsed = [item.strip() for item in file.readlines()]

        for vehicle in vehicles:
            vehicle: Export

            if vehicle.vehicle_id in parsed:
                continue

            contact = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Хочу купить', callback_data=f'helpwith {vehicle.vehicle_id}')]
            ])

            await bot.send_photo(chat_id=-1001887191619,  # -1001837912591 856367900
                                 photo=vehicle.picture,
                                 caption=f'<b>{vehicle.title}</b>\n\n'
                                         f'<b>Цена:</b> {vehicle.price}\n'
                                         f'<b>Локация:</b> {vehicle.location}\n'
                                         f"<b>Информация:</b> {vehicle.info}\n\n",
                                 parse_mode=ParseMode.HTML,
                                 reply_markup=contact)

            file.write(vehicle.vehicle_id + '\n')
