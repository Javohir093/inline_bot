from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# reset_bot=ReplyKeyboardMarkup(resize_keyboard=True, botton=[
#     [KeyboardButton(text=" Ботни қайта ишга тушириш")]])

markup=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💲Автомобил нархлари", callback_data="prise_auto")],
    [InlineKeyboardButton(text="ℹ️ Сотувда борлиги тогрисида малумот", callback_data="sell_info")],
    [InlineKeyboardButton(text="🆕 Сунги янгиликлар", callback_data="news")],
    [InlineKeyboardButton(text="🚘 Автомобиллар информацияси", callback_data="car_info")]
])

page_2=InlineKeyboardBuilder()
page_2.row(InlineKeyboardButton(text="Chevrolet", callback_data="chevrolet"))
page_2.row(InlineKeyboardButton(text="Hyundai", callback_data="hyundai"))
page_2.row(InlineKeyboardButton(text="Lada", callback_data="lada"))
page_2.row(InlineKeyboardButton(text="Kia", callback_data="kia"))
page_2.row(InlineKeyboardButton(text="BYD", callback_data="byd"))
page_2.row(InlineKeyboardButton(text="⬅️ Ortga", callback_data="back1"))

chevrolet_cars=0




