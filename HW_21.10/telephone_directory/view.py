from file_processing import read_file
import telebot.types
from bot_ import *


def get_type(msg: telebot.types.Message):
    t = msg.text
    if t != '1' and t != '2':
        bot.send_message(chat_id=msg.from_user.id, text='Незнакомый формат, ввеедите заново')
        bot.register_next_step_handler(msg, callback=get_type)
    else:
        view_data(t, msg.from_user.id)


def view_data(t, id_):
    t = int(t)
    data = read_file()
    message = ''
    if t == 1:
        for person in data:
            message += '\n'.join(person)
            message += '\n\n'
    else:
        for person in data:
            message += ', '.join(person)
            message += '\n'
    bot.send_message(chat_id=id_, text=message)