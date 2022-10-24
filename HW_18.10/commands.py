from authorization import log_in
import data
import hw


def command(c, authorized):
    if authorized:
        role = data.database[authorized]['роль']
    if c == 'exit':
        data.save()
        return 'break'
    if not authorized:
        if c == 'log in':
            return log_in()
        print("Недоступная комманда.")
        return False
    if c == 'show homework':
        hw.show_hw()
        return ''
    if c == 'help':
        help_(role)
        return ''
    if c == 'students':
        show_students()
        return ''
    if role == 't' and c == 'add homework':
        hw.add_hw()
        return ''
    print('Недоступная команда.')
    return ''


def help_(role):
    print("""
Список доступных комманд:
exit - выход из программы
help - вывод списка программ
show homework - вывестии домашнее задание
students - вывести список студентов""")
    if role == 't':
        print("add homework - добавить домашнее задание\n")


def show_students():
    grade = input('Введите номер класса, список студентов которого хотите увидеть, '
                  'или введите {все}, чтобы вывести список всех студентов: ')
    d = {}
    if grade == 'все':
        for login in data.database.keys():
            if data.database[login]['роль'] == 's':
                if int(data.database[login]['класс']) not in d.keys():
                    d[int(data.database[login]['класс'])] = [f"{data.database[login]['фамилия']}"
                                                        f" {data.database[login]['имя']}"
                                                        f" {data.database[login]['отчество']}"]
                else:
                    d[int(data.database[login]['класс'])].append(f"{data.database[login]['фамилия']}"
                                                            f" {data.database[login]['имя']}"
                                                            f" {data.database[login]['отчество']}")
    else:
        for login in data.database.keys():
            if data.database[login]['роль'] == 's':
                if data.database[login]['класс'] == grade:
                    if int(data.database[login]['класс']) not in d.keys():
                        d[int(data.database[login]['класс'])] = [f"{data.database[login]['фамилия']}"
                                                            f" {data.database[login]['имя']}"
                                                            f" {data.database[login]['отчество']}"]
                    else:
                        d[int(data.database[login]['класс'])].append(f"{data.database[login]['фамилия']}"
                                                                f" {data.database[login]['имя']}"
                                                                f" {data.database[login]['отчество']}")
    if not d:
        print("Ничего не найдено")
    else:
        for g in sorted(d.keys()):
            print(f"{g} класс")
            for name in sorted(d[g]):
                print(name)
            print()
