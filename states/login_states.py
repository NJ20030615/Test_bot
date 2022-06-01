from aiogram.dispatcher.filters.state import StatesGroup, State


class LoginState(StatesGroup):
    name = State()
    date_of_birth = State()
    davlat = State()
    viloyat = State()
    tuman = State()
    mahalla = State()
    ish_joyi = State()
    number = State()
