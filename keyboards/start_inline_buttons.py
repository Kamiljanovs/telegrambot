from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Опросник",
        callback_data="start_questionnaire"
    )
    ban_check_button = InlineKeyboardButton(
        "Проверить себя",
        callback_data="ban_check"
    )
    markup.add(questionnaire_button)
    markup.add(ban_check_button)
    return markup

