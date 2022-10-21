from file_processing import read_file


def view_data():
    t = input('Ввеедите формат (1 или 2): ')
    while t != '1' and t != '2':
        t = input('Незнакомый формат, ввеедите заново: ')
    t = int(t)
    data = read_file()
    if t == 1:
        for person in data:
            for el in person:
                print(el)
            print()
    else:
        for person in data:
            print(', '.join(person))
        print()
