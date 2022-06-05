from datetime import datetime
from random import randint

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from keraksiz import new_test, length
from loader import dp, db
from keyboards.inline.login import login_keyboard, login_keyboard_2, login_keyboard_3
from keyboards.inline.test import button_test, answers_button
from keyboards.default.login import button_phone_number
from keyboards.default.main_page import button_main
from states.login_states import LoginState


@dp.callback_query_handler(text='kanallar_check', state='*')
async def check(call: types.CallbackQuery):
    await call.message.edit_text(text="Yana bir bor botimizga xush kelibsiz.\nDavom ettirish uchun"
                                      " ro'yxatdan o'tinsh tugmasini bosing.",
                                 reply_markup=login_keyboard())


@dp.callback_query_handler(text="Ro'yxatdan o'tish", state="*")
async def name(message: types.CallbackQuery):
    await message.message.edit_text(f"Familiya/Ism/Sharifingizni kiriting:\n"
                                    f"Misol uchun:  Azizova Aziza Aziz qizi")
    await LoginState.name.set()


@dp.message_handler(state=LoginState.name)
async def name(message: types.Message):
    await message.answer(f"Tug'ilgan sanangizni kiriting:\n"
                         f"Misol uchun:  29.02.2003")
    db.update_user_Name(message.from_user.id, message.text)
    await LoginState.date_of_birth.set()


@dp.message_handler(state=LoginState.date_of_birth)
async def date_of_birth(message: types.Message, state: FSMContext):
    sana = message.text
    if len(sana) != 10:
        await message.answer("Siz sanani noto'g'ri formatda kiritdingiz.\nIltimos sanani quyidagi formatda "
                             "kiriting: 29.02.2003")
    else:
        if sana[2] == '.' and sana[5] == '.' and 1996 < int(sana[6:]) <= 2006:
            await message.answer("Qaysi viloyatda yashaysiz?", reply_markup=login_keyboard_2())
            await LoginState.viloyat.set()
            db.update_user_sana(message.from_user.id, sana)
        else:
            if sana[2] == '.' and sana[5] == '.' and len(sana) == 10:
                await message.answer("Afsuski, bu tanlovda yosh oralig'i 16-25 yosh qilib belgilangan.\n"
                                     "Davom ettirish uchun /start tugmasini bosing.")
                await state.finish()
                await state.reset_state()
                db.select_user_by_id(message.from_user.id)
            else:
                await message.answer("Siz sanani noto'g'ri formatda kiritdingiz.\nIltimos sanani quyidagi formatda "
                                     "kiriting: 29.02.2003")


@dp.callback_query_handler(state=LoginState.viloyat)
async def davlat(call: types.CallbackQuery):
    await call.answer(call.data)
    await call.message.edit_text(f"Qaysi tumanda yashaysiz?", reply_markup=login_keyboard_3(call.data))
    db.update_user_viloyat(call.from_user.id, call.data)
    await LoginState.tuman.set()


@dp.callback_query_handler(state=LoginState.tuman)
async def tuman(call: types.CallbackQuery):
    await call.answer(call.data)
    await call.message.edit_text(f"Yashash manzilingizni kiriting?\nMisol uchun: Tangatopdi, Bog' MFY, 20-uy")
    await LoginState.mahalla.set()
    db.update_user_tuman(call.from_user.id, call.data)


@dp.message_handler(state=LoginState.mahalla)
async def mahalla(call: types.Message):
    await call.answer(f"Ish yoki o'qish joyingizni kiriting:\nMisol uchun: Talaba, "
                      f"Toshkent axborot texnologiyalari unversiteti")
    await LoginState.ish_joyi.set()
    db.update_user_mahalla(call.from_user.id, call.text)


@dp.message_handler(state=LoginState.ish_joyi)
async def number(call: types.Message):
    await call.answer(f"Telefon raqamingizni yuborish uchun tugmani bosing", reply_markup=button_phone_number)
    db.update_user_work_place(call.from_user.id, call.text)


@dp.message_handler(state=LoginState.ish_joyi, content_types=['contact'])
async def echo(message: types.Message, state: FSMContext):
    await message.answer(f"Tabriklaymiz! Siz ro'yxatdan muvoffaqqiyatli o'tdingiz", reply_markup=ReplyKeyboardRemove())
    await state.finish()
    await state.reset_state()
    db.update_user_telephone(message.from_user.id, message.contact.phone_number)
    await message.answer("Botdan foydalanish uchun quyidagi tugmalardan birini bosing:", reply_markup=button_main)


@dp.message_handler(text="ℹ️ Ma'lumot")
async def info(message: types.Message):
    await message.answer("Bot uchun ma'lumot:", )


@dp.message_handler(text="👤 Profilim")
async def profile(message: types.Message):
    user = db.select_user_by_id(message.from_user.id)
    await message.answer(f"👤 Sizning profilingiz:\n\n"
                         f"👤 {user[1]}\n"
                         f"📞 {user[7]}\n"
                         f"📅 {user[2]}\n"
                         f"🏠 {user[3]}\n"
                         f"🏠 {user[4]}\n"
                         f"🏠 {user[5]}\n"
                         f"🏢 {user[6]}\n")


@dp.message_handler(text="🔢 Natijam")
async def natijam(message: types.Message):
    user = db.select_user_by_id(message.from_user.id)
    if user[9] == "0":
        await message.answer("Siz hozzircha test yechmagansiz")
    else:
        await message.answer(f"Sizning natijangiz: {user[8]} ball")


@dp.message_handler(text="🔠 Test ishlash")
async def test(message: types.Message):
    user = db.select_user_by_id(message.from_user.id)
    if user[9] == "0":
        await message.answer("Testni ishlash uchun quyidagi tugmani bosing:", reply_markup=button_test())
        tests = []
        while len(tests) < 50:
            test_number = randint(0, length())
            if test_number not in tests:
                tests.append(test_number)
        s = ""
        for i in tests:
            s = s + str(i) + " "
        db.update_user_status(message.from_user.id, s)
        db.update_user_date(message.from_user.id, datetime.now())
    else:
        await message.answer(f"Siz test yechib bo'ldingiz.\nSizning natijangiz: {user[8]} ball")


@dp.callback_query_handler(text="test")
async def test(call: types.CallbackQuery):
    tests = new_test("baza.txt")
    await call.message.edit_text(f"Test boshlandi:")
    db.update_user_score(call.from_user.id, "0")
    i = 0
    number = db.select_user_by_id(call.from_user.id)[9]
    number += f"{i}"
    db.update_user_status(call.from_user.id, number)
    text = f"{i+1}) {tests[int(i)][0]}\n{tests[int(i)][1][0]}\n{tests[int(i)][2][0]}\n{tests[int(i)][3][0]}\n" \
           f"{tests[int(i)][4][0]}\n{tests[int(i)][5][0]}"
    correct_answer = ""
    if tests[int(i)][1][1] == "1":
        correct_answer = "A"
    elif tests[int(i)][2][1] == "1":
        correct_answer = "B"
    elif tests[int(i)][3][1] == "1":
        correct_answer = "C"
    elif tests[int(i)][4][1] == "1":
        correct_answer = "D"
    elif tests[int(i)][5][1] == "1":
        correct_answer = "E"
    await call.message.answer(text, reply_markup=answers_button(correct_answer))


@dp.callback_query_handler(text="T")
@dp.callback_query_handler(text="F")
async def true(call: types.CallbackQuery):
    tests = new_test("baza.txt")
    user = db.select_user_by_id(call.from_user.id)
    date = user[10]
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    timedifference = datetime.now() - date
    timedifference = timedifference.seconds
    if timedifference > 1200:
        await call.message.edit_text(f"Testni ishlash vaqti tugadi.", )
    else:
        number = db.select_user_by_id(call.from_user.id)[9]
        test_numbers = number.split(" ")
        i = int(test_numbers[-1]) + 1
        if i == 50:
            await call.message.edit_text(f"Test tugadi. Natijalarni ko'rish uchun 🔢 Natijam Tugmasini bosing.")
        else:
            test_numbers.pop()
            test_numbers.append(str(i))
            number = ""
            for j in test_numbers:
                number = number + j + " "
            number = number[:-1]
            db.update_user_status(call.from_user.id, number)
            if call.data == "T":
                score = int(db.select_user_by_id(call.from_user.id)[8]) + 1
                db.update_user_score(call.from_user.id, score)
                await call.answer("✅")
            else:
                await call.answer("❌")
            j = int(number.split(" ")[i])
            text = f"{int(i)+1}) {tests[int(j)][0][tests[int(j)][0].find('.')+1:]}\n{tests[int(j)][1][0]}\n" \
                   f"{tests[int(j)][2][0]}\n{tests[int(j)][3][0]}\n{tests[int(j)][4][0]}\n{tests[int(j)][5][0]}"
            correct_answer = ""
            if tests[int(i)][1][1] == "1":
                correct_answer = "A"
            elif tests[int(i)][2][1] == "1":
                correct_answer = "B"
            elif tests[int(i)][3][1] == "1":
                correct_answer = "C"
            elif tests[int(i)][4][1] == "1":
                correct_answer = "D"
            elif tests[int(i)][5][1] == "1":
                correct_answer = "E"
            await call.message.edit_text(text, reply_markup=answers_button(correct_answer))


@dp.message_handler(text="JASURBEK", state="*")
async def test(message: types.Message):
    db.admin()
    await message.answer("Jasurbek")
