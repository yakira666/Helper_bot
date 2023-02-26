import os

import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import default_comands

load_dotenv(".env")
BOT_TOKEN = os.environ.get("API_TOKEN")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(
    filename="log_file.log",
    level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()
dp.include_router(default_comands.router)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
