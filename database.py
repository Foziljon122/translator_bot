import sqlite3
from datetime import datetime                           


connection = sqlite3.connect('users.db')
sql = connection.cursor()



sql.execute("create table if not exists user(id integer  PRIMARY KEY AUTOINCREMENT,first_name text, telegram_id text,phone_number text,reg_date DATETIME)")
sql.execute("create table if not exists Use_Word(id integer  PRIMARY KEY AUTOINCREMENT,telegram_id text, text text,trans_text text,reg_date DATETIME)")




def register_user(telegram_id, first_name, phone_namber):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()

    sql.execute("INSERT INTO user (telegram_id, first_name, phone_number, reg_date) VALUES (?,?,?,?);", (telegram_id, first_name,phone_namber, datetime.now()))

    connection.commit()
    connection.close()

def check_user(telegram_id):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()

    user = sql.execute("SELECT telegram_id FROM user WHERE telegram_id=? ", (telegram_id,)). fetchone()

    if user:
        return True
    else:
        return False
    
print(check_user(12345))

def add_user_words(telegram_id, text, translated_text):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()

    sql.execute('INSTER INTO user_words (telegram_id, text, translated_text, added_date) VALUES (?,?,?,?);')
    (telegram_id,text,translated_text,datetime.datetime.now())

    connection.commit()
    connection.close()

                