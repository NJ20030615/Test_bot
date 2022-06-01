from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔠 Test ishlash"),
            KeyboardButton(text="🔢 Natijam")
        ],
        [
            KeyboardButton(text="👤 Profilim"),
            KeyboardButton(text="ℹ️ Ma'lumot")
        ],
    ],
    resize_keyboard=True
)