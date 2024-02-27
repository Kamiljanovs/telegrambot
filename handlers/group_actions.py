import datetime

from aiogram import types, Dispatcher

import database.bot_db
from config import bot, GROUP_ID
from keyboards import questionnaire_inline_buttons
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    db = database.bot_db.Database()
    if message.chat.id == int(GROUP_ID):
        ban_words_prob = predict_prob([message.text])
        print(ban_words_prob)

        if ban_words_prob > 0.8:
            potential = db.sql_select_ban_user(
                tg_id=message.from_user.id
            )

            if not potential:
                db.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )
            elif potential['count'] >= 3:
                # await bot.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                #     until_date=datetime.datetime.now() + datetime.timedelta(hours=1)
                # )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Пользователь: {message.from_user.first_name} заблокирован\n"
                         f"Количество нарушений: {potential['count']}"
                )
            else:
                db.sql_update_ban_count(
                    tg_id=message.from_user.id
                )
            await message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=f'Привет {message.from_user.first_name}\n'
                     f'Не сквернословь в нашем чате!'
            )

async def check_ban(call: types.CallbackQuery):
    db = database.bot_db.Database()
    user = db.sql_select_ban_user(
        call.from_user.id,
    )

    if not user:
        await call.message.answer(
            f'Вас нету в списке банов, не волнуйтесь'
        )
    else:
        text=f'Вы были записаны {user["count"]} раз, будьте аккуратнее.'
        await call.message.answer(text)

def register_group_actions_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        check_ban,
        lambda call: call.data == 'ban_check'
    )
    dp.register_message_handler(
        chat_messages
    )
