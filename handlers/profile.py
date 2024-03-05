import sqlite3
from aiogram import types, Dispatcher

import const
from config import bot
from const import PROFILE_TEXT
from database.bot_db import Database
from keyboards.profile_inline_buttons import (
    my_profile_keyboard,
    like_dislike_keyboard
)
import random
import re


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
    # print(update_profile_call)

async def delete_profile_call(call: types.CallbackQuery):
    db = Database()
    db.sql_delete_profile(
        tg_id=call.from_user.id
    )
    await call.message.answer(
        "Ваш профиль удален"
    )

async def random_filter_profile_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_all_profiles(
        tg_id=call.from_user.id
    )
    # print(profiles)
    if not profiles:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Вы уже просмотрели все профили, приходите позже!"
        )
        return

    random_profile = random.choice(profiles)
    with open(random_profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=const.PROFILE_TEXT.format(
                nickname=random_profile['nickname'],
                biography=random_profile['biography'],
                age=random_profile['age'],
                zodiac_sign=random_profile['zodiac_sign'],
                hobby=random_profile['hobby'],
                gender=random_profile['gender'],
            ),
            reply_markup=await like_dislike_keyboard(
                tg_id=random_profile['telegram_id']
            )
        )

async def detect_like_call(call: types.CallbackQuery):
    owner = re.sub("like_", "", call.data)
    db = Database()
    try:
        db.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Вы уже лайкнули этот профиль!"
        )
        return
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)




def register_profile_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        delete_profile_call,
        lambda call: call.data == "delete_profile"
    )
    dp.register_callback_query_handler(
        random_filter_profile_call,
        lambda call: call.data == "random_profiles"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: 'like_' in call.data
    )