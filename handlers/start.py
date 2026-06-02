from email import message
from aiogram import F

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
    
@router.message(F.text == "📚 FAQ")
async def faq(message: Message):

    await message.answer(
        "📚 FAQ\n\n"
        "❓ Как задать вопрос?\n"
        "→ Нажмите '🤖 Задать вопрос'\n\n"
        "❓ Когда отвечает поддержка?\n"
        "→ Обычно в течение дня"
    )


@router.message(F.text == "📞 Поддержка")
async def support_info(message: Message):

    await message.answer(
        "📞 Поддержка\n\n"
        "Ответ оператора поступит "
        "прямо в этом чате."
    )  
    

@router.message(F.text == "ℹ️ О сервисе")
async def about(message: Message):

    await message.answer(
        "ℹ️ AI Support Bot\n\n"
        "Бот для обработки обращений "
        "и поддержки пользователей.\n\n"
        "Stack:\n"
        "Python + Aiogram + PostgreSQL"
    )    
    

