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

async def like_dislike_keyboard(tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Лайк",
        callback_data=f"like_{tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Дизлайк",
        callback_data=f"skip_{tg_id}"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup




