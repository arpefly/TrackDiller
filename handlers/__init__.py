from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from .start import start_command
from .configure_search import configure_search_button
from .vehicle_condition import vehicle_condition_callback
from .vehicle_category import vehicle_category_callback
from .vehicle_brand import vehicle_brand_callback
from .help_with import help_with_callback
from .others import other_text


def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(configure_search_button, Text(equals=['Настроить поиск']))
    dp.register_callback_query_handler(vehicle_condition_callback, Text(startswith='vehicle_condition'))
    dp.register_callback_query_handler(vehicle_category_callback, Text(startswith='category'))
    dp.register_callback_query_handler(vehicle_brand_callback, Text(startswith='brand'))
    dp.register_callback_query_handler(help_with_callback, Text(startswith='helpwith'))
    dp.register_message_handler(other_text)
