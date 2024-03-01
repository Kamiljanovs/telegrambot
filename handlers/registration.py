from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_buttons
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    hobby = State()
    gender = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Напишите свой никнейм!"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Напишите пару слов о себе."
    )
    await RegistrationStates.next()

async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько тебе лет?\n"
             "Отправь свой возрат только цифрами.\n"
             "Например: 27 или 23."
    )
    await RegistrationStates.next()

async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Регистрация провалена.\n"
                 "Повторите попытку!\n"
                 "Отправьте свой возрат только цифрами.\n"
                 "Например: 27 или 23."
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = int(message.text)
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Теперь назовите свой знак зодиака."
    )
    await RegistrationStates.next()


async def load_zodiac_sign(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['zodiac_sign'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text="А какое у вас хобби?"
    )
    await RegistrationStates.next()

async def load_hobby(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Укажите свой пол?"
    )
    await RegistrationStates.next()

async def load_gender(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправьте свое фото в фото формате."
    )
    await RegistrationStates.next()

async def load_photo(message: types.Message,
                     state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )

    async with (state.proxy() as data):
        user = db.sql_select_profile(
            message.from_user.id
        )
        if not user:
            db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            biography=data['biography'],
            age=data['age'],
            zodiac_sign=data['zodiac_sign'],
            hobby=data['hobby'],
            gender=data['gender'],
            photo=path.name
        )
        else:
            db.sql_update_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                biography=data['biography'],
                age=data['age'],
                zodiac_sign=data['zodiac_sign'],
                hobby=data['hobby'],
                gender=data['gender'],
                photo=path.name
            )
        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    biography=data['biography'],
                    age=data['age'],
                    zodiac_sign=data['zodiac_sign'],
                    hobby=data['hobby'],
                    gender=data['gender']
                )
            )
    if not user:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Вы успешно зарегистрировались!"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Ваш профиль обновился.")
    await state.finish()

def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_hobby,
        state=RegistrationStates.hobby,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "update_profile"
    )