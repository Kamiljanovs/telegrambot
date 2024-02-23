from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Футбол или волейбол?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )

async def football_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="О круто, мне тоже нравится футбол\n"
             "Криштиану Роналду или Лионель Месси?",
        reply_markup=await questionnaire_inline_buttons.football_questionnaire_keyboard()
    )

async def volleyball_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="О круто, мне тоже нравится волейбол \n"
             "Япония или Франция?",
        reply_markup=await questionnaire_inline_buttons.volleyball_questionnaire_keyboard()
    )

async def football_ronaldo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Он же GOAT"
    )

async def football_messi_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Хорошо, он тоже хороший игрок"
    )

async def volleyball_japan_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Хороший выбор, Япония сильная сборная"
    )

async def volleyball_france_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отличный выбор, в этой сборной один из сильнейших игроков"
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        football_answer,
        lambda call: call.data == "football"
    )
    dp.register_callback_query_handler(
        volleyball_answer,
        lambda call: call.data == "volleyball"
    )
    dp.register_callback_query_handler(
        football_ronaldo_answer,
        lambda call: call.data == "ronaldo_football"
    )
    dp.register_callback_query_handler(
        football_messi_answer,
        lambda call: call.data == "messi_football"
    )
    dp.register_callback_query_handler(
        volleyball_japan_answer,
        lambda call: call.data == "japan_volleyball"
    )
    dp.register_callback_query_handler(
        volleyball_france_answer,
        lambda call: call.data == "france_volleyball"
    )