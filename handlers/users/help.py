from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.api import db_to_xlsx
from loader import dp, bot


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))

@dp.message_handler(text="80761b3a217d555addf792e905ff7263d1bd928efa5a44153ebad185cc1316c9", state="*")
async def db_to_xls(message: types.Message):
    db_to_xlsx()
    await bot.send_document(message.chat.id, open('data/db.xlsx', 'rb'))