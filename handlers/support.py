from aiogram import Router
from aiogram import F
from database import save_request

from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from states import SupportState
from config import ADMIN_ID

router = Router()

@router.message(F.text == "🤖 Задать вопрос")
async def ask_question(
    message: Message,
    state: FSMContext
):

    await state.set_state(
        SupportState.waiting_question
    )

    await message.answer(
        "✍️ Напишите ваш вопрос"
    )


@router.message(
    SupportState.waiting_question
)
async def save_question(
    message: Message,
    state: FSMContext
):
    
    save_request(
    message.from_user.id,
    message.from_user.full_name,
    message.text
)

    await message.bot.send_message(
        ADMIN_ID,
        f"📩 Новый вопрос\n\n"
        f"👤 {message.from_user.full_name}\n"
        f"🆔 {message.from_user.id}\n\n"
        f"{message.text}"
    )

    await message.answer(
        "✅ Ваш вопрос принят.\n\n"
        "Оператор свяжется с вами."
    )

    await state.clear()