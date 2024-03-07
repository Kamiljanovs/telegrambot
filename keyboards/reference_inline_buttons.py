from aiogram import Dispatcher
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Сгенерируй ссылку",
        callback_data="reference_link"
    )
    list_button = InlineKeyboardButton(
        "Список рефералов",
        callback_data="reference_list"
    )
    markup.add(list_button)
    return markup

