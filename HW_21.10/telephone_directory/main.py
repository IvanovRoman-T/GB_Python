import export_import
from add import *
import view
import telebot.types
from bot_ import *


@bot.message_handler(commands=['formats'])
def first_help(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="""
Формат 1:
    Фамилия_1
    Имя_1
    Телефон_1
    Описание_1

    Фамилия_2
    Имя_2
    Телефон_2
    Описание_2

Формат 2:
    Фамилия_1,Имя_1,Телефон_1,Описание_1
    Фамилия_2,Имя_2,Телефон_2,Описание_2
    """)


@bot.message_handler(commands=['add'])
def add_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите фамилию")
    bot.register_next_step_handler(msg, callback=get_surname)


@bot.message_handler(commands=['view'])
def view_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Ввеедите формат (1 или 2)')
    bot.register_next_step_handler(msg, callback=view.get_type)


@bot.message_handler(commands=['export'])
def export_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Ввеедите формат (1 или 2)')
    bot.register_next_step_handler(msg, callback=export_import.get_type)


@bot.message_handler(commands=['import'])
def import_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Пришлите импортируемый файл.')
    bot.register_next_step_handler(msg, callback=export_import.import_file)


@bot.message_handler(commands=['help'])
def help_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="""
Список доступных комманд:
/add - добавление записи вручную с клавиатуры
/view - просмотр записей
/export - экспортирование сохранённых записей в файл
/import - добавление новых записей из файла
/help - вывод допустимых комманд
/formats - вывод допустимых форматов
    """)


bot.polling()


