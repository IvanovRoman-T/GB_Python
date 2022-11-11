import file_processing as fp
import telebot.types
from bot_ import *


surname = ''
name = ''
number = ''
description = ''


def get_surname(msg: telebot.types.Message):
    global surname
    surname = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя")
    bot.register_next_step_handler(msg, get_name)


def get_name(msg: telebot.types.Message):
    global name
    name = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите номер")
    bot.register_next_step_handler(callback=get_number, message=msg)


def get_number(msg: telebot.types.Message):
    global number
    number = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите описание")
    bot.register_next_step_handler(callback=get_descr, message=msg)


def get_descr(msg: telebot.types.Message):
    global description
    description = msg.text
    add_record(msg.from_user.id)


def add_record(id_):
    p = (surname, name, number, description)
    data = fp.read_file()
    data.add(p)
    fp.write_file(data, 'data.txt')
    bot.send_message(chat_id=id_, text='Запись успешно добавлена.\n')
