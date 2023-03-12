import asyncio
import random

from aiogram.utils.exceptions import RetryAfter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, Message

from create_bot import bot, db
from utils import TestVehicleSeller
from utils import convert
from otomoto import otomoto_volvo_trackors
from olx import olx_all_tandems
from olx import olx_all_tractors
from classes import Export


async def broadcast():
    currencies = convert()
    vehicles = []

    print('-' * 30)
    vehicles += otomoto_volvo_trackors(*currencies)
    print(f'len(vehicles): {len(vehicles)}')
    vehicles += olx_all_tandems(*currencies)
    print(f'len(vehicles): {len(vehicles)}')
    vehicles += olx_all_tractors(*currencies)
    print(f'len(vehicles): {len(vehicles)}')
    print(f'total len: {len(vehicles)}')
    print('-' * 30, end='\n\n')

    for vehicle in vehicles:
        vehicle: Export

        if db.vehicle_exists(site_name=vehicle.site_name, vehicle_id=vehicle.vehicle_id):
            continue

        contact = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Получить консультацию', callback_data=f'buy {vehicle.site_name} {vehicle.vehicle_id}')]
        ])

        message = Message()
        try:
            if len(vehicle.photos.split(';')) >= 2:
                try:
                    await bot.send_media_group(chat_id=TestVehicleSeller,
                                               media=[InputMediaPhoto(media=vehicle.photos.split(';')[0],
                                                                      caption=f'<b>{vehicle.title}</b>\n\n'
                                                                              f'<b>Цена:</b> {vehicle.price if vehicle.price != 0 else "уточняйте при консультации"} $\n'
                                                                              f'<b>Год выпуска:</b> {vehicle.year}\n'
                                                                              f'<b>Коробка передач:</b> {vehicle.transmission}\n')] +
                                                     [InputMediaPhoto(media=pic) for pic in vehicle.photos.split(';')][1:],
                                               disable_notification=True)

                    await bot.send_message(chat_id=TestVehicleSeller,
                                           text=f'<b>Получить консультацию по {vehicle.title}</b>',
                                           reply_markup=contact,
                                           disable_notification=True)
                except RetryAfter as ex:
                    await asyncio.sleep(ex.timeout + 20)
                    await bot.send_media_group(chat_id=TestVehicleSeller,
                                               media=[InputMediaPhoto(media=vehicle.photos.split(';')[0],
                                                                      caption=f'<b>{vehicle.title}</b>\n\n'
                                                                              f'<b>Цена:</b> {vehicle.price if vehicle.price != 0 else "уточняйте при консультации"} $\n'
                                                                              f'<b>Год выпуска:</b> {vehicle.year}\n'
                                                                              f'<b>Коробка передач:</b> {vehicle.transmission}\n')] +
                                                     [InputMediaPhoto(media=pic) for pic in vehicle.photos.split(';')][1:],
                                               disable_notification=True)

                    await bot.send_message(chat_id=TestVehicleSeller,
                                           text=f'<b>Получить консультацию по {vehicle.title}</b>',
                                           reply_markup=contact,
                                           disable_notification=True)
            else:
                await bot.send_photo(chat_id=TestVehicleSeller,
                                     photo=vehicle.photos,
                                     caption=f'<b>{vehicle.title}</b>\n\n'
                                             f'<b>Цена:</b> {vehicle.price} $\n'
                                             f'<b>Год выпуска:</b> {vehicle.year}\n'
                                             f'<b>Коробка передач:</b> {vehicle.transmission}\n',
                                     reply_markup=contact,
                                     disable_notification=True)
        except RetryAfter as ex:
            print(ex)
            await asyncio.sleep(ex.timeout + 20)

        db.add_vehicle(site_name=vehicle.site_name, export=vehicle)
        await asyncio.sleep(20 + random.randint(2, 7))
