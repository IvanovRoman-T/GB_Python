from bot_ import bot
import telebot.types
from expression import *
from calculate import *
import time


@bot.message_handler(commands=['help'])
def help_(msg: telebot.types.Message):
    with open("log.txt", 'a') as f:
        f.write(f"{time.ctime(time.time())} {msg.from_user.id} {msg.from_user.username} {msg.text}\n")
        t = """Введите выражение, чтобы его посчитать
Например: (2 + 6i) * (-1 + i)
Скобки и порядок вещественной и мнимой части обязательны"""
        bot.send_message(chat_id=msg.from_user.id, text=t)
        f.write("reply:\n" + time.ctime(time.time()) + " " + t + "\n\n")


@bot.message_handler()
def calc(msg: telebot.types.Message):
    with open("log.txt", 'a') as f:
        f.write(f"{time.ctime(time.time())} {msg.from_user.id} {msg.from_user.username} {msg.text}\n")
        e = get_expression(msg.text)
        if ['', ''] in e or msg.text.count('(') != 2 or msg.text.count(')') != 2:
            bot.send_message(chat_id=msg.from_user.id, text="Некорректный ввод")
            f.write("reply:\n" + time.ctime(time.time()) + " Некорректный ввод" + "\n\n")
        else:
            a = operation(e)
            if a == '':
                f.write("reply:\n" + time.ctime(time.time()) + " Некорректный ввод" + "\n\n")
                a = "Некорректный ввод"
            f.write("reply:\n" + time.ctime(time.time()) + ' ' + a + "\n\n")
            bot.send_message(chat_id=msg.from_user.id, text=a)


bot.polling()
