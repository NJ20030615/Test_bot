from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def kanallar_keyboard():
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Alisher Sadullayev", url="https://t.me/alisher_sadullaev"),
            InlineKeyboardButton(text="IBRAT tillar oromgohi", url="https://t.me/ibratcamp_uz"),
        ],
        [
            InlineKeyboardButton(text="Obunani tekshirish", callback_data="kanallar_check"),
        ],
        ])
    return keys

def support():
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Support", url="https://t.me/ibratcamp2022supportbot"),
        ],
    ])
    return keys