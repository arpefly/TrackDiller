from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

vehicle_condition = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Неважно', callback_data='vehicle_condition.Beliebig')],
    [InlineKeyboardButton(text='Новая', callback_data='vehicle_condition.Neu')],
    [InlineKeyboardButton(text='Подержанная', callback_data='vehicle_condition.Gebraucht')]
])
