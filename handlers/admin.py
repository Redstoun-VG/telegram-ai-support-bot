from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import admin_keyboard
from aiogram import F

from config import ADMIN_ID
from database import get_requests

router = Router()


@router.message(
    Command("requests")
)
async def requests_list(
    message: Message
):

    if message.from_user.id != ADMIN_ID:

        return

    requests = get_requests()

    if not requests:

        await message.answer(
            "📭 Обращений пока нет"
        )

        return

    text = "📩 Обращения\n\n"

    for request in requests:

        text += (
            f"🆔 {request[0]}\n"
            f"👤 {request[2]}\n"
            f"❓ {request[3]}\n\n"
        )

    await message.answer(text)


@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "🔐 Админ панель",
        reply_markup=admin_keyboard
    )


@router.message(F.text == "📊 Статистика")
async def stats(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    requests = get_requests()

    await message.answer(
        f"📊 Статистика\n\n"
        f"📩 Всего обращений: {len(requests)}"
    )  


@router.message(F.text == "📩 Обращения")
async def requests_button(
    message: Message
):

    if message.from_user.id != ADMIN_ID:
        return

    requests = get_requests()

    if not requests:

        await message.answer(
            "📭 Обращений пока нет"
        )

        return

    text = "📩 Обращения\n\n"

    for request in requests:

        text += (
            f"🆔 {request[0]}\n"
            f"👤 {request[2]}\n"
            f"❓ {request[3]}\n\n"
        )

    await message.answer(text)      
