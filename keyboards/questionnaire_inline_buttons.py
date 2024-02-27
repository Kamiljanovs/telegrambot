from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    football_button = InlineKeyboardButton(
        "Футбол",
        callback_data="football"
    )
    volleyball_button = InlineKeyboardButton(
        "Волейбол",
        callback_data="volleyball"
    )
    markup.add(football_button)
    markup.add(volleyball_button)
    return markup

async def football_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    ronaldo_button = InlineKeyboardButton(
        "Роналду",
        callback_data="ronaldo_football"
    )
    messi_button = InlineKeyboardButton(
        "Месси",
        callback_data="messi_football"
    )
    markup.add(ronaldo_button)
    markup.add(messi_button)
    return markup

async def volleyball_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    japan_button = InlineKeyboardButton(
        "Япония",
        callback_data="japan_volleyball"
    )
    france_button = InlineKeyboardButton(
        "Франция",
        callback_data="france_volleyball"
    )
    markup.add(japan_button)
    markup.add(france_button)
    return markup
