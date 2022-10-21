import file_processing as fp


def add_record():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    number = input("Введите номер: ")
    description = input("Введите описание: ")
    p = (surname, name, number, description)
    data = fp.read_file()
    data.add(p)
    fp.write_file(data, 'data.txt')
    print('Запись успешно добавлена.\n')
