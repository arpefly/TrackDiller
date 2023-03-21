import asyncio
import random

from aiogram.utils.exceptions import RetryAfter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputFile, Message

from create_bot import bot, db
from utils import TestVehicleSeller, VehicleSeller
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

        try:
            if len(vehicle.photos.split(';')) >= 2:
                try:
                    await bot.send_media_group(chat_id=VehicleSeller,
                                               media=[InputMediaPhoto(media=InputFile(vehicle.photos.split(';')[0]),
                                                                      caption=f'<b>{vehicle.title}</b>\n\n'
                                                                              f'<b>Цена:</b> {vehicle.price if vehicle.price != 0 else "уточняйте при консультации"} $\n'
                                                                              f'<b>Год:</b> {vehicle.year}\n'
                                                                              f'<b>Коробка:</b> {vehicle.transmission}\n\n'
                                                                              '<b>Консультация: @smmbahtiiar</b>')] +
                                                     [InputMediaPhoto(media=InputFile(pic)) for pic in vehicle.photos.split(';')][1:10])

                    await bot.send_message(chat_id=VehicleSeller,
                                           text=f'<b>Получить консультацию по {vehicle.title}</b>\n\n'
                                                '<b>Консультация: @smmbahtiiar</b>',
                                           reply_markup=contact)
                except RetryAfter as ex:
                    print(f'1 {ex}')
                    await asyncio.sleep(ex.timeout + 20)
                    await bot.send_media_group(chat_id=VehicleSeller,
                                               media=[InputMediaPhoto(media=InputFile(vehicle.photos.split(';')[0]),
                                                                      caption=f'<b>{vehicle.title}</b>\n\n'
                                                                              f'<b>Цена:</b> {vehicle.price if vehicle.price != 0 else "уточняйте при консультации"} $\n'
                                                                              f'<b>Год:</b> {vehicle.year}\n'
                                                                              f'<b>Коробка:</b> {vehicle.transmission}\n\n'
                                                                              '<b>Консультация: @smmbahtiiar</b>')] +
                                                     [InputMediaPhoto(media=InputFile(pic)) for pic in vehicle.photos.split(';')][1:10])

                    await bot.send_message(chat_id=VehicleSeller,
                                           text=f'<b>Получить консультацию по {vehicle.title}</b>\n\n'
                                                '<b>Консультация: @smmbahtiiar</b>',
                                           reply_markup=contact)
            elif len(vehicle.photos.split(';')) == 1:
                if vehicle.photos.split(';')[0] == '':
                    continue
                await bot.send_photo(chat_id=VehicleSeller,
                                     photo=InputFile(vehicle.photos.split(';')[0]),
                                     caption=f'<b>{vehicle.title}</b>\n\n'
                                             f'<b>Цена:</b> {vehicle.price} $\n'
                                             f'<b>Год:</b> {vehicle.year}\n'
                                             f'<b>Коробка:</b> {vehicle.transmission}\n\n'
                                             '<b>Консультация: @smmbahtiiar</b>',
                                     reply_markup=contact)
            else:
                continue
        except RetryAfter as ex:
            print(f'2 {ex}')
            await asyncio.sleep(ex.timeout + 20)

        db.add_vehicle(export=vehicle)
        await asyncio.sleep(20 + random.randint(2, 7))
