import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType

from dotenv import load_dotenv

load_dotenv("../.env")
BOT_TOKEN: str = os.environ.get("API_TOKEN")
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(f"Привет\nМеня зовут эхо бот\nНапиши мне что-нибудь!")


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(f"Напиши мне что-нибудь, и в ответ я отправлю тебе такое же сообщение!")


@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


@dp.message()
async def send_echo(message: Message):
    await message.answer(text=message.text)
    # await bot.send_message(message.chat.id, message.text)
    # await bot.send_message(chat_id='ID или название чата', text='Какой-то текст')


# dp.message.register(process_start_command, Command(commands=["start"]))
# dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_echo)
if __name__ == "__main__":
    dp.run_polling(bot)
