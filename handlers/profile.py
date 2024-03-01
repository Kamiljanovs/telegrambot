import sqlite3
from aiogram import types, Dispatcher

import const
from config import bot
from const import PROFILE_TEXT
from database.bot_db import Database
from keyboards.profile_inline_buttons import my_profile_keyboard


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_profile(
        tg_id=call.from_user.id
    )
    if profile:
        with open(profile['photo'],'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    biography=profile['biography'],
                    age=profile['age'],
                    zodiac_sign=profile['zodiac_sign'],
                    hobby=profile['hobby'],
                    gender=profile['gender'],
                ),
                reply_markup=await my_profile_keyboard()
            )
    else:
        await bot.send_message(
            call.from_user.id,
            text="Вы еще не зарегестрированы.\n"
                 "Пожалуйста сперва пройдите регистрацию, чтобы увидеть свой профиль."
        )
async def update_profile_call(call: types.CallbackQuery):
    db = Database()
    db.sql_update_profile(
        tg_id=call.from_user.id
    )
    print(update_profile_call)

async def delete_profile_call(call: types.CallbackQuery):
    db = Database()
    db.sql_delete_profile(
        tg_id=call.from_user.id
    )
    await call.message.answer(
        "Ваш профиль удален"
    )

def register_profile_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    # dp.register_callback_query_handler(
    #     update_profile_call,
    #     lambda call: call.data == "update_profile"
    # )
    dp.register_callback_query_handler(
        delete_profile_call,
        lambda call: call.data == "delete_profile"
    )