import file_processing as fp


def export_data():
    file_name = input('Введите название файла в формате {название_файла.txt}: ')
    if file_name[len(file_name) - 4:] != '.txt':
        file_name = input('Незнакомый формат файла. Введите название файла в формате {название_файла.txt}: ')
    t = input('Ввеедите формат (1 или 2): ')
    while t != '1' and t != '2':
        t = input('Незнакомый формат, ввеедите заново: ')
    t = int(t)
    fp.write_file(fp.read_file(), file_name, t)
    print(f'Файл {file_name} успешно сохранён.\n')


def import_file():
    file_name = input('Введите путь к файлу:\n')
    while True:
        try:
            f = open(file_name, 'r')
        except FileNotFoundError:
            file_name = input('Файл не найден. Введите путь заново:\n')
            continue
        break
    # t = input('Ввеедите формат (1 или 2): ')
    # while t != '1' and t != '2':
    #     t = input('Незнакомый формат, ввеедите заново: ')
    # t = int(t)
    addition = fp.read_file(file_name, 2)
    if len(list(addition)[0]) != 4:
        addition = fp.read_file(file_name, 1)
    data = fp.read_file()
    data = data.union(addition)
    fp.write_file(data, 'data.txt', 1)
    print(f'Файл {file_name} успешно импортирован.\n')
