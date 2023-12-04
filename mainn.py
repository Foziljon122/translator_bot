import telebot

import database
import buttons

from telebot.types import  ReplyKeyboardRemove
from googletrans import Translator
translator = Translator()

TOKEN = "6137523219:AAHZlYmIGOw4JiwTRtnrfSuAowfeKNfxXbY"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):

    user = database.check_user(message.from_user.id)

    if user:
        bot.send_message(message.from_user.id, 'To start translate, user the button', reply_markup=buttons.translate_button())

    else:
        bot.send_message(message.from_user.id, 'To start the using the bot, share your contact!', reply_markup=buttons.contact_button())
        bot.register_next_step_handler(message, get_contact)


def get_contact(message):
    if message.contact:
        user_phone = message.contact.phone_number
        first_name = message.contact.first_name
        telegram_id = message.from_user.id

        database.register_user(telegram_id, first_name, user_phone)

        bot.send_message(message.from_user.id, 'To start translate, user the button', reply_markup=buttons.translate_button())

    else:
        bot.send_message(message.from_user.id, 'Please to share your contact use the button', reply_markup=buttons.contact_button())
        bot.register_next_step_handler(message, get_contact)



@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Translate🔄':
        bot.send_message(message.from_user.id, 'Choice which language you want to', reply_markup=buttons.language_buttons())
        bot.register_next_step_handler(message, get_language)

def get_language(message):
    to_language = message.text

    bot.send_message(message.from_user.id, 'Send text to translate', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translate_text, to_language)

def translate_text(message, to_language):
    text = message.text

    result = translator.translate(text=text, dest=to_language).text

    bot.send_message(message.from_user.id, result, reply_markup=buttons.translate_button())


bot.polling()