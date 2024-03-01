from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    update_button = InlineKeyboardButton(
        "Обновить",
        callback_data="update_profile"
    )
    delete_button = InlineKeyboardButton(
        "Удалить",
        callback_data="delete_profile"
    )
    markup.add(update_button)
    markup.add(delete_button)
    return markup




