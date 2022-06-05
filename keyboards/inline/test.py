from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def button_test():
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Testni boshlash", callback_data="test"),
        ],
    ])
    return keys


def answers_button(answer):
    answer_A = InlineKeyboardButton(text="A", callback_data="F")
    answer_B = InlineKeyboardButton(text="B", callback_data="F")
    answer_C = InlineKeyboardButton(text="C", callback_data="F")
    answer_D = InlineKeyboardButton(text="D", callback_data="F")
    answer_E = InlineKeyboardButton(text="E", callback_data="F")
    if answer == "A":
        answer_A = InlineKeyboardButton(text="A", callback_data="T")
    if answer == "B":
        answer_B = InlineKeyboardButton(text="B", callback_data="T")
    if answer == "C":
        answer_C = InlineKeyboardButton(text="C", callback_data="T")
    if answer == "D":
        answer_D = InlineKeyboardButton(text="D", callback_data="T")
    if answer == "E":
        answer_E = InlineKeyboardButton(text="E", callback_data="T")
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            answer_A,
            answer_B,
            answer_C,
            answer_D,
            answer_E,
        ],
    ])
    return keys
