from aiogram import Bot, Dispatcher, executor
import asyncio
import sqlite3
from database import sql_queries

from config import dp
from handlers import (
    start,
    questionnaire,
    group_actions,
    registration,
    profile,
    reference,
)
from database import bot_db

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite3.db')
        self.cursor = self.conn.cursor()

    async def sql_create_tables(self):
        try:
            await self.cursor.execute(sql_queries.CREATE_USER_TABLE_QUERY)
            await self.cursor.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
            # await self.cursor.execute(sql_queries.CREATE_NEWS_LINK_QUERY)
            # await self.cursor.execute(sql_queries.CREATE_ASYNC_NEWS_LINK_QUERY)
            await self.conn.commit()

        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")


async def on_startup(_):
    await init_database()


async def init_database():
    try:
        db = bot_db.Database()
        await db.sql_create_tables()
    except asyncio.TimeoutError:
        print("Ошибка: Превышено время ожидания для инициализации базы данных")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profile.register_profile_handler(dp=dp)
reference.register_reference_handlers(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup
    )
