from googletrans import Translator

translator = Translator()


# result = translator.translate('Hi', dest="uz").text

# print(result)

def transs(text,language):
    trans = Translator()
    result = trans.translate(text,dest=language).text
    print(result)

while True:
    text = input('INTER text to translate to: ')
    to_language = input('Inter language to translate: ')
    transs(text,to_language)


def register_user(telegram_id, first_name, phone_namber):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    sql.execute()