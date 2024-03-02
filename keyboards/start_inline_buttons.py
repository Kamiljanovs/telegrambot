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
    registration_button = InlineKeyboardButton(
        "Регистрация",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой профиль",
        callback_data="my_profile"
    )
    profiles_button = InlineKeyboardButton(
        "Смотреть профили",
        callback_data="random_profiles"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(profiles_button)
    return markup

