import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.kanallar import kanallar_keyboard


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(message.from_user.id, "", "", "", "", "", "", "", "", "")
        await message.answer(f"{name}, bizning botimizga xush kelibsiz!\nBotdan foydalanish uchun quyidagi "
                                 f"kanallarga a'zo bo'ling.", reply_markup=kanallar_keyboard())
    except sqlite3.IntegrityError as err:
        pass

    # #Adminga xabar beramiz
    # count = db.count_users()[0]
    # msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
