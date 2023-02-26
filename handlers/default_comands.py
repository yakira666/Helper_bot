from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!")
