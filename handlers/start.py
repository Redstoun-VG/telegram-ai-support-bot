from email import message

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import FSInputFile

from keyboards import main_keyboard

router = Router()



@router.message(CommandStart())
async def start(message: Message):


    photo = FSInputFile(
    "images/welcome.png"
)

    await message.answer_photo(
    photo=photo,
    caption=
    "🤖 Добро пожаловать в AI Support Bot!\n\n"
    "Ваш умный помощник всегда на связи 🚀",
    reply_markup=main_keyboard
)
    
    

