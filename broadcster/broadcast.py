import asyncio
import random

import aiogram.utils.exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, ParseMode

from create_bot import bot, db
from config import VehicleSeller, TestVehicleSeller
from otomoto import otomoto_volvo_trackors
from classes import Export


async def broadcast():
    vehicles = []

    vehicles += otomoto_volvo_trackors()

    for vehicle in vehicles:
        vehicle: Export

        if db.vehicle_exists(site_name=vehicle.site_name, vehicle_id=vehicle.vehicle_id):
            continue

        contact = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Получить консультацию', callback_data=f'buy {vehicle.site_name} {vehicle.vehicle_id}')]
        ])

        try:
            if len(vehicle.photos.split(';')) >= 2:
                await bot.send_media_group(chat_id=VehicleSeller,
                                           media=[InputMediaPhoto(media=vehicle.photos.split(';')[0],
                                                                  caption=f'<b>{vehicle.title}</b>\n\n'
                                                                          f'<b>Цена:</b> {vehicle.price} $\n'
                                                                          f'<b>Локация:</b> {vehicle.location}\n'
                                                                          f'<b>Описание:</b> {vehicle.info}',
                                                                  parse_mode=ParseMode.HTML)] +
                                                 [InputMediaPhoto(media=pic) for pic in vehicle.photos.split(';')][1:])

                await bot.send_message(chat_id=VehicleSeller,
                                       text=f'<b>Получить консультацию по {vehicle.title}</b>',
                                       parse_mode=ParseMode.HTML,
                                       reply_markup=contact)
            else:
                await bot.send_photo(chat_id=VehicleSeller,
                                     photo=vehicle.photos,
                                     caption=f'<b>{vehicle.title}</b>\n\n'
                                             f'<b>Цена:</b> {vehicle.price} $\n'
                                             f'<b>Локация:</b> {vehicle.location}\n'
                                             f'<b>Описание:</b> {vehicle.info}',
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=contact)
        except aiogram.utils.exceptions.RetryAfter as ex:
            print(ex)
            await asyncio.sleep(ex.timeout + random.randint(0, 5))

        db.add_vehicle(site_name='otomoto', export=vehicle)
        await asyncio.sleep(10 + random.randint(0, 5))
