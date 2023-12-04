from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton ('Share contact', request_contact=True)

    kb.add(button)
    return kb

def translate_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    buttonn = KeyboardButton('Translate🔄')
    kb.add(buttonn)

    return kb

def language_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    ru = KeyboardButton('Ru')
    uz = KeyboardButton('Uz')
    en = KeyboardButton('En')
    es = KeyboardButton('Es')

    kb.add(ru, uz, en, es)
    return kb   
