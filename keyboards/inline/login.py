from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def login_keyboard():
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Ro‘yxatdan o‘tish", callback_data="Ro'yxatdan o'tish"),
        ],
    ])
    return keys


def login_keyboard_2():
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Andijon", callback_data="Andijon"),
            InlineKeyboardButton(text="Namangan", callback_data="Namangan"),
        ],
        [
            InlineKeyboardButton(text="Farg‘ona", callback_data="Farg'ona"),
            InlineKeyboardButton(text="Jizzax", callback_data="Jizzax"),
        ],
        [
            InlineKeyboardButton(text="Sirdaryo", callback_data="Sirdaryo"),
            InlineKeyboardButton(text="Surxondaryo", callback_data="Surxondaryo"),
        ],
        [
            InlineKeyboardButton(text="Qashqadaryo", callback_data="Sirdaryo"),
            InlineKeyboardButton(text="Xorazm", callback_data="Xorazm"),
        ],
        [
            InlineKeyboardButton(text="Buxoro", callback_data="Buxoro"),
            InlineKeyboardButton(text="Samarqand", callback_data="Samarqand"),
        ],
        [
            InlineKeyboardButton(text="Navoiy", callback_data="Navoiy"),
            InlineKeyboardButton(text="Toshkent", callback_data="Toshkent"),
        ],
        [
            InlineKeyboardButton(text="Toshkent viloyati", callback_data="Toshkent viloyati"),
        ],
        [
            InlineKeyboardButton(text="Qoraqalpog'iston respublikasi", callback_data="Qoraqalpog'iston respublikasi"),
        ],
    ])
    return keys


tumanlar = {"Andijon": ["Andijon shahri", "Asaka tumani", "Baliqchi tumani", "Bo'ston tumani", "Buloqboshi tumani",
                        "Izboskan tumani", "Jalaquduq tumani", "Xo'jaobod tumani", "Qo'rg'ontepa tumani",
                        "Marhamat tumani",
                        "Oltinko'l tumani", "Paxtaobod tumani", "Shahrixon tumani", "Ulug'nor tumani"],
            "Namangan": ["Chortoq tumani", "Chust tumani", "Davlatobod tumani", "Kosonsoy tumani", "Mingbuloq tumani",
                         "Namangan shahri", "Namangan tumani", "Norin tumani", "Pop tumani", "To'raqo'rg'on tumani",
                         "Uchqo'rg'on tumani", "Uychi tumani", "Yangiqo'rgon tumani"],
            "Farg'ona": ["Beshariq tumani", "Bog'dod tumani", "Buvayda tumani", "Dang'ara tumani", "Farg'ona shahri",
                         "Farg'ona tumani", "Furqat tumani", "Marg'ilon shahri", "O'zbekiston tumani",
                         "Oltiariq tumani",
                         "Qo'qon shahri", "Qo'shtepa tumani", "Quva tumani", "Quvasoy shahri", "Rishton tumani",
                         "So'x tumani", "Toshloq tumani", "Uchko'prik tumani", "Yozyovon tumani"],
            "Jizzax": ["Arnasoy tumani", "Baxmal tumani", "Do'stlik tumani", "Forish tumani", "G'allaorol tumani",
                       "Jizzax shahri", "Jizzax tumani", "Mirzacho'l tumani", "Paxtakor tumami", "Yangiobod tumani",
                       "Zafarobod tumani", "Zarband tumani", "Zomin tumani"],
            "Sirdaryo": ["Boyovut tumani", "Guliston shahri", "Guliston tumani", "Oqoltin tumani", "Sardoba tumani",
                         "Sayxunobod tumani", "Shirin shahri", "Sirdaryo tumani", "Xovos tumani", "Yangiyer shahri"],
            "Surxondaryo": ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqo'rg'on tumani",
                            "Muzrobot tumani", "Oltinsoy tumani", "Qiziriq tumani", "Qumqo'rg'on tumani",
                            "Sariosiyo tumani", "Sherobod tumani", "Sho'rchi tumani", "Termiz shahri", "Termiz tumani",
                            "Uzun tumani"],
            "Qashqadaryo": ["Chiroqchi tumani", "Dehqonobod tumani", "G'uzor tumani", "Kasbi tumani", "Kitob tumani",
                            "Koson tumani", "Mirishkor tumani", "Muborat tumani", "Nishon tumani", "Qamashi tumani",
                            "Qarshi shahri", "Qarshi tumani", "Shahrisabz tumani", "Yakkabog' tumani"],
            "Xorazm": ["Bog'ot tumani", "Gurlan tumani", "Qo'shko'pir tumani", "Shovot tumani", "Tuproqqala tumani ",
                       "Urganch shahri", "Urganch tumani", "Xazorasp tumani", "Xiva tumani", "Xonqa tumani",
                       "Yangiariq tumani", "Yangibozor tumani"],
            "Buxoro": ["Buxoro shahri", "Buxoro tumani", "G'ijduvon tumani", "Jondor tumani", "Kogon shahri",
                       "Kogon tumani", "Olot tumani", "Peshku tumani", "Qorako'l tumani", "Qorovulbozor tumani",
                       "Romitan tumani", "Shofirkon tumani", "Vobkent tumani"],
            "Samarqand": ["Bulung'ur tumani", "Ishtixon tumani", "Jomboy tumani", "Kattaqo'rg'on shahri",
                          "Kattaqo'rg'on tumani", "Narpay tumani", "Nurobod tumani", "Oqdaryo tumani",
                          "Past darg'om tumani", "Paxtachi tumani", "Payariq tumani", "Qo'shrabot tumani",
                          "Samarqand shahri", "Samarqand tumani", "Toyloq tumani", "Urgut tumani"],
            "Navoiy": ["Karmana tumani", "Konimex tumani", "Navbahor tumani", "Navoiy shahri", "Nurota tumani",
                       "Qiziltepa tumani", "Tomdi tumani", "Uchquduq tumani", "Xatirchi tumani", "Zarafshon shahri"],
            "Toshkent": ["Bektemir tumani", "Chilonzor tumani", "Mirobod tumani", "Mirzo Ulug'bek tumani",
                         "Olmazor tumani", "Sergeli tumani", "Shayhontohur tumani", "Uchtepa tumani",
                         "Yakkasaroy tumani", "Yashnaobod tumani", "Yunusobod tumani", "Yangihayot tumani"],
            "Toshkent viloyati": ["Angren shahri", "Bekobod shahri", "Bekobod tumani", "Bo'ka tumani",
                                  "Bo'stonliq tumani", "Chinoz tumani", "Chirchiq shahri", "Nurafshon shahar", 
                                  "O'rta chirchiq tumani", "Ohangaron tumani", "Olmaliq shahri", "Oqqo'rg'on tumani", 
                                  "Parkent tumani", "Piskent tumani", "Qibray tumani", "Quyi chirchiq tumani", 
                                  "Toshkent tumani", "Yangiyo'l tumani", "Yuqori chirchiq tumani", "Zangiota tumani"],
            "Qoraqalpog'iston respublikasi": ["Amudaryo tumani", "Beruniy tumani", "Chimboy tumani", "Ellikqala tumani",
                                              "Kegeyli tumani", "Mo'ynoq tumani", "Nukus shahri", "Nukus tumani",
                                              "Qonliko'l tumani", "Qorauzaq tumani", "Qung'irot tumani",
                                              "Shumanay tumani", "Taxiatosh tumani", "Taxtako'pir tumani",
                                              "To'rtko'l tumani", "Xo'jayli tumani", "Bo‘zatov tumani"]
            }


def login_keyboard_3(tuman):
    inline_key = []
    new_tuman = []
    for tuman_nomi in tumanlar[tuman]:
        if len(new_tuman) == 1:
            new_tuman.append(InlineKeyboardButton(text=tuman_nomi, callback_data=tuman_nomi))
            inline_key.append(new_tuman)
            new_tuman = []
        else:
            new_tuman.append(InlineKeyboardButton(text=tuman_nomi, callback_data=tuman_nomi))
    inline_key.append(new_tuman)
    keys = InlineKeyboardMarkup(inline_keyboard=inline_key)
    return keys
