from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
keyboard=[
[
KeyboardButton(
text="🤖 Задать вопрос"
)
],
[
KeyboardButton(
text="📚 FAQ"
),
KeyboardButton(
text="📞 Поддержка"
)
],
[
KeyboardButton(
text="ℹ️ О сервисе"
)
]
],
resize_keyboard=True
)



admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📊 Статистика"
            )
        ],
        [
            KeyboardButton(
                text="📩 Обращения"
            )
        ]
    ],
    resize_keyboard=True
)