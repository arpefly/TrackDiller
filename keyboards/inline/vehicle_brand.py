from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

vehicle_brand = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Beliebig', callback_data='brand.Beliebig'), InlineKeyboardButton(text='DAF', callback_data='brand.DAF'), InlineKeyboardButton(text='Demag', callback_data='brand.Demag')],
    [InlineKeyboardButton(text='Faun', callback_data='brand.Faun'), InlineKeyboardButton(text='Ford', callback_data='brand.Ford'), InlineKeyboardButton(text='Freightliner', callback_data='brand.Freightliner')],
    [InlineKeyboardButton(text='FUSO', callback_data='brand.FUSO'), InlineKeyboardButton(text='Ginaf', callback_data='brand.Ginaf'), InlineKeyboardButton(text='Grove', callback_data='brand.Grove')],
    [InlineKeyboardButton(text='Hako', callback_data='brand.Hako'), InlineKeyboardButton(text='HN Schörling', callback_data='brand.HN Schörling'), InlineKeyboardButton(text='Iveco', callback_data='brand.Iveco')],
    [InlineKeyboardButton(text='Kamaz', callback_data='brand.Kamaz'), InlineKeyboardButton(text='Liebherr', callback_data='brand.Liebherr'), InlineKeyboardButton(text='Mack', callback_data='brand.Mack')],
    [InlineKeyboardButton(text='Magirus Deutz', callback_data='brand.Magirus Deutz'), InlineKeyboardButton(text='MAN', callback_data='brand.MAN'), InlineKeyboardButton(text='Meiller', callback_data='brand.Meiller')],
    [InlineKeyboardButton(text='Mercedes-Benz', callback_data='brand.Mercedes-Benz'), InlineKeyboardButton(text='Mitsubishi', callback_data='brand.Mitsubishi'), InlineKeyboardButton(text='Nissan', callback_data='brand.Nissan')],
    [InlineKeyboardButton(text='Opel', callback_data='brand.Opel'), InlineKeyboardButton(text='Palfinger', callback_data='brand.Palfinger'), InlineKeyboardButton(text='Peugeot', callback_data='brand.Peugeot')],
    [InlineKeyboardButton(text='Renault', callback_data='brand.Renault'), InlineKeyboardButton(text='Ruthmann', callback_data='brand.Ruthmann'), InlineKeyboardButton(text='Scania', callback_data='brand.Scania')],
    [InlineKeyboardButton(text='Schmidt', callback_data='brand.Schmidt'), InlineKeyboardButton(text='Skoda', callback_data='brand.Skoda'), InlineKeyboardButton(text='Steyr', callback_data='brand.Steyr')],
    [InlineKeyboardButton(text='Tatra', callback_data='brand.Tatra'), InlineKeyboardButton(text='Toyota', callback_data='brand.Toyota'), InlineKeyboardButton(text='Unimog', callback_data='brand.Unimog')],
    [InlineKeyboardButton(text='Volkswagen', callback_data='brand.Volkswagen'), InlineKeyboardButton(text='Volvo', callback_data='brand.Volvo'), InlineKeyboardButton(text='Yanmar', callback_data='brand.Yanmar')],
    [InlineKeyboardButton(text='Andere', callback_data='brand.Andere')]
])
