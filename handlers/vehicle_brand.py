import time

from aiogram.types import CallbackQuery

from selenium_worker import get_links
from selenium.webdriver.common.by import By
from selenium_worker.create_selenium import driver


async def vehicle_brand_callback(callback: CallbackQuery):
    await callback.answer()
#     search_config.vehicle_brand = callback.data.split('.')[1]
#
#     await callback.message.answer('Начинаю поиск')
#     await callback.answer()
#     await callback.message.delete()
#
#     link_to_parse = get_links.get_mobile_link(search_config)
#     driver.get('https://suchen.mobile.de/fahrzeuge/search.html?c=OtherTruckOver7500&con=USED&fr=2011%3A2013&isSearchRequest=true&ml=400000%3A500000&ms=17200%3B%3B%3B%3B&ref=dsp&s=Truck&vc=TruckOver7500')
#     time.sleep(1)
#
#     for item in driver.find_element(By.CLASS_NAME, 'cBox-body--resultitem').find_elements(By.CLASS_NAME, 'cBox-body--resultitem'):
#         name = item.find_element(By.CLASS_NAME, 'u-text-break-word').text
#         price = item.find_element(By.CLASS_NAME, 'u-block').text
#
#         await callback.message.answer(name + ' ' + price)
