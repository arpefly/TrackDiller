from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from .start import start_command
from .buy import help_with_callback
from .others import other_text


def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(help_with_callback, Text(startswith='buy'))
    dp.register_message_handler(other_text)
