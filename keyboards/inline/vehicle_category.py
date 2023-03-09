from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

vehicle_category = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Beliebig', callback_data='category.Beliebig'), InlineKeyboardButton(text='Abrollkipper', callback_data='category.RollOffTipperTruck')],
    [InlineKeyboardButton(text='Abschleppwagen', callback_data='category.BreakdownTruck'), InlineKeyboardButton(text='Absetzkipper', callback_data='category.DumperTruck')],
    [InlineKeyboardButton(text='Autokran', callback_data='category.TruckMountedCraneTruck'), InlineKeyboardButton(text='Autotransporter', callback_data='category.CarCarrierTruck')],
    [InlineKeyboardButton(text='Betonmischer', callback_data='category.CementMixerTruck'), InlineKeyboardButton(text='Betonpumpe', callback_data='category.ConcretePump')],
    [InlineKeyboardButton(text='Dreiseitenkipper', callback_data='category.Over7500_ThreeSidedTipper'), InlineKeyboardButton(text='Fahrgestell', callback_data='category.ChassisTruck')],
    [InlineKeyboardButton(text='Getränkewagen', callback_data='category.BeveragesTruck'), InlineKeyboardButton(text='Getreidekipper', callback_data='category.GrainTruck')],
    [InlineKeyboardButton(text='Holztransporter', callback_data='category.TimberCarrierTruck'), InlineKeyboardButton(text='Hubarbeitsbühne', callback_data='category.HydraulicWorkPlatformTruck')],
    [InlineKeyboardButton(text='Jumbo-Lkw', callback_data='category.JumboTruck'), InlineKeyboardButton(text='Kehrmaschine', callback_data='category.SweepingMachineTruck')],
    [InlineKeyboardButton(text='Kipper', callback_data='category.TipperTruck'), InlineKeyboardButton(text='Koffer', callback_data='category.BoxTruck')],
    [InlineKeyboardButton(text='Kühlkoffer', callback_data='category.RefrigeratorBodyTruck'), InlineKeyboardButton(text='Lebensmitteltankwagen', callback_data='category.MilkTankTruck')],
    [InlineKeyboardButton(text='Muldenkipper', callback_data='category.SkipLorryTruck'), InlineKeyboardButton(text='Müllwagen', callback_data='category.RefuseTruck')],
    [InlineKeyboardButton(text='Pritsche', callback_data='category.StakeBodyTruck'), InlineKeyboardButton(text='Pritsche + Plane', callback_data='category.StakeBodyAndTarpaulinTruck')],
    [InlineKeyboardButton(text='Saug- und Druckwagen', callback_data='category.VacuumAndPressureVehicleTruck'), InlineKeyboardButton(text='Tankwagen', callback_data='category.TankBodiesTruck')],
    [InlineKeyboardButton(text='Tier-/Pferdetransportwagen', callback_data='category.HorsesTruck'), InlineKeyboardButton(text='Verkaufsaufbau', callback_data='category.TrafficConstructionTruck')],
    [InlineKeyboardButton(text='Wechselfahrgestell', callback_data='category.SwapChassisTruck'), InlineKeyboardButton(text='Andere Lkw über 7,5 t', callback_data='category.OtherTruckOver7500')],
])
