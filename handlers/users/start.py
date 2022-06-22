import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.kanallar import kanallar_keyboard


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    try:
        db.add_user(message.from_user.id, "", "", "", "", "", "", "", "", "")
        await message.answer("Yoshlar ishlari agentligi tillarni o‘rta (B1) va undan yuqori darajada biladigan yoshlar "
                             "uchun IBRAT LANGUAGE CAMP yozgi oromgohini tashkil qilmoqda!\n\nIBRAT LANGUAGE CAMP yozgi"
                             " oromgohi 16 yoshdan 25 yoshgacha bo‘lgan yoshlar uchun:\n- chet tillari bo‘yicha nazariy"
                             " mashg‘ulotlarni o‘tkazish;\n- yoshlar bilan amaliy ish tajribasini almashish;\n- xorijiy"
                             " tillarda so'zlashuvchi yoshlar hamjamiyatini yaratish maqsadlarida tashkil etiladi.\n\n"
                             "1. Oromgoh bepul va 7 kun davom etadi. Toshkent shaxrigacha bo'lgan yo'l xarajatlarini "
                             "o'zingiz qoplaysiz. Qolgan barcha xarajatlar Yoshlar ishlari agentligi tomonidan "
                             "qoplanadi.\n\n2. Oromgohga qabul qilishda rasmiy sertifikatlar majburiy emas. Tilni "
                             "bilish darajangiz minimum B1 (4.0,4.5,5.0)bo’lishi kerak. Bu baholarni tasdiqlovchi "
                             "sertifikat bo’lmagan taqdirda ham, test va suhbat orqali sizdan alohida sinov imtixoni "
                             "olinadi.\n\n❗️"
                             "Barcha ishtrokchilarga imkon berish maqsadida 2021-yil Ibrat oromgohida ishtrokchi "
                             "sifatida qatnashganlar, bu yilgi(2022 yil) Ibrat oromgohida qatnashish imkoniga ega "
                             "emaslar.")
        await message.answer(f"Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling.",
                             reply_markup=kanallar_keyboard())
    except sqlite3.IntegrityError as err:
        await message.answer("Yoshlar ishlari agentligi tillarni o‘rta (B1) va undan yuqori darajada biladigan yoshlar "
                             "uchun IBRAT LANGUAGE CAMP yozgi oromgohini tashkil qilmoqda!\n\nIBRAT LANGUAGE CAMP yozgi"
                             " oromgohi 16 yoshdan 25 yoshgacha bo‘lgan yoshlar uchun:\n- chet tillari bo‘yicha nazariy"
                             " mashg‘ulotlarni o‘tkazish;\n- yoshlar bilan amaliy ish tajribasini almashish;\n- xorijiy"
                             " tillarda so'zlashuvchi yoshlar hamjamiyatini yaratish maqsadlarida tashkil etiladi.\n\n"
                             "1. Oromgoh bepul va 7 kun davom etadi. Toshkent shaxrigacha bo'lgan yo'l xarajatlarini "
                             "o'zingiz qoplaysiz. Qolgan barcha xarajatlar Yoshlar ishlari agentligi tomonidan "
                             "qoplanadi.\n\n2. Oromgohga qabul qilishda rasmiy sertifikatlar majburiy emas. Tilni "
                             "bilish darajangiz minimum B1 (4.0,4.5,5.0)bo’lishi kerak. Bu baholarni tasdiqlovchi "
                             "sertifikat bo’lmagan taqdirda ham, test va suhbat orqali sizdan alohida sinov imtixoni "
                             "olinadi.\n\n❗️"
                             "Barcha ishtrokchilarga imkon berish maqsadida 2021-yil Ibrat oromgohida ishtrokchi "
                             "sifatida qatnashganlar, bu yilgi(2022 yil) Ibrat oromgohida qatnashish imkoniga ega "
                             "emaslar.")
        await message.answer(f"Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling.",
                             reply_markup=kanallar_keyboard())

    # #Adminga xabar beramiz
    # count = db.count_users()[0]
    # msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
