from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamimni yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

