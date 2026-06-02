import asyncio
from handlers.support import router as support_router
from handlers.admin import router as admin_router

from aiogram import Bot
from aiogram import Dispatcher

from config import TOKEN
from handlers.start import router as start_router

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(
    support_router
)

dp.include_router(
    admin_router
)

dp.include_router(start_router)

async def main():

    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())