import file_processing as fp
import telebot.types
from bot_ import *


def get_type(msg: telebot.types.Message):
    t = msg.text
    if t != '1' and t != '2':
        bot.send_message(chat_id=msg.from_user.id, text='Незнакомый формат, ввеедите заново')
        bot.register_next_step_handler(msg, callback=get_type)
    else:
        export_data(t, msg.from_user.id)


def export_data(t, id_):
    t = int(t)
    fp.write_file(fp.read_file(), 'export.txt', t)
    bot.send_document(chat_id=id_, document=open('export.txt', 'rb'))


def import_file(msg: telebot.types.Message):
    if msg.content_type == 'document':
        file = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file.file_path)
        with open(msg.document.file_name, 'wb') as f:
            f.write(downloaded_file)
        addition = fp.read_file(msg.document.file_name, 2)
        if len(list(addition)[0]) != 4:
            addition = fp.read_file(msg.document.file_name, 1)
        data = fp.read_file()
        data = data.union(addition)
        fp.write_file(data, 'data.txt', 1)
        bot.send_message(chat_id=msg.from_user.id, text='Файл успешно импортирован.')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали не документ. Для импортирования, вызовите команду повторно.')
