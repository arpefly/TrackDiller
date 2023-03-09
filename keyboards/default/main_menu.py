from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Добавить сайт')]
    ],
    resize_keyboard=True
)
