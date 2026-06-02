from email import message

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):


    await message.answer(
    "🤖 Добро пожаловать в AI Support Bot!\n\n"
    "Здесь вы сможете получать ответы на вопросы и поддержку.",
    reply_markup=main_keyboard
)

