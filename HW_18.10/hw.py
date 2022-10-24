import data


def show_hw():
    subject = input('Введите название предмета, по которому хотите увидеть домашнее задание, '
                    'или введите {все}, чтобы вывести домашнее задание по всем предметам: ')
    date = input('Введите дату, на которую хотите увидеть домашнее задание, '
                 'или введите {все}, чтобы вывести домашнее задание на все даты: ')
    if subject == 'все':
        if date == 'все':
            for s in data.homework.keys():
                print(f"Домашнее задание по предмету {s}:")
                for d in data.homework[s].keys():
                    print(f"{d}: {data.homework[s][d]}")
                print()
        else:
            print(f"Домашнее задание на {date}:")
            for s in data.homework.keys():
                if date in data.homework[s].keys():
                    print(f"{s}: {data.homework[s][date]}")
    elif subject in data.homework.keys():
        if date == 'все':
            print(f"Домашнее задание по предмету {subject}:")
            for d in data.homework[subject].keys():
                print(f"{d}: {data.homework[subject][d]}")
        elif date in data.homework[subject].keys():
            print(f"Домашнее задание по предмету {subject} на {date}: {data.homework[subject][date]}")
        else:
            print("Пока ничего нет")
    else:
        print("Пока ничего нет")


def add_hw():
    subject = input('Введите название предмета, по которому хотите добавить домашнее задание: ')
    while True:
        date = input('Введите дату в формате ДД.ММ, на которую хотите добавить домашнее задание: ')
        if len(date) == 5 and date[2] == '.' and (date[:2] + date[3:]).isdigit() and \
                int(date[3:]) < 13 and int(date[:2]) < 32:
            break
        print('Некорректная дата.')
    mode = input('Введите {a}, чтобы добавить задание к существующему или {w},'
                 ' чтобы изменить или создать новое задание: ')
    hw = input("Введите текст задания: ")
    if mode == 'w':
        data.homework[subject][date] = hw
    else:
        if subject in data.homework.keys():
            if date in data.homework[subject].keys():
                data.homework[subject][date] += ';' + hw
            else:
                data.homework[subject][date] = hw
        else:
            data.homework[subject][date] = hw
    print("Задание добавлено.\n")