# Создайте программу для игры в ""Крестики-нолики"".


def win(f):
    for i in f:
        if i == ['X'] * 3:
            return 'X'
        elif i == ['0'] * 3:
            return '0'
    for i in list(zip(f[0], f[1], f[2]))[0]:
        if i == ('X',) * 3:
            return 'X'
        elif i == ('0',) * 3:
            return '0'
    if f[0][0] == f[1][1] == f[2][2] == 'X' or f[0][2] == f[1][1] == f[2][0] == 'X':
        return 'X'
    elif f[0][0] == f[1][1] == f[2][2] == '0' or f[0][2] == f[1][1] == f[2][0] == '0':
        return 'X'
    for i in f:
        for j in i:
            if j != 'X' and j != '0':
                return ''
    return 'n'


def print_field(f):
    f = list(map(lambda x: list(map(str, x)), f))
    print('' + ' | '.join(f[0]))
    print('-' * 11)
    print('' + ' | '.join(f[1]))
    print('-' * 11)
    print('' + ' | '.join(f[2]))


def move(i, f):
    if not i % 2:
        while True:
            inp = int(input("Куда поставить X?   "))
            if f[(inp - 1) // 3][inp % 3 - 1] != 'X' and f[(inp - 1) // 3][inp % 3 - 1] != '0':
                f[(inp - 1) // 3][inp % 3 - 1] = 'X'
                return f
            if not 0 < inp < 10:
                print("Эта позиция не существует")
            else:
                print("Эта позиция занята")
    else:
        while True:
            inp = int(input("Куда поставить 0?   "))
            if f[(inp - 1) // 3][inp % 3 - 1] != 'X' and f[(inp - 1) // 3][inp % 3 - 1] != '0':
                f[(inp - 1) // 3][inp % 3 - 1] = '0'
                return f
            if not 0 < inp < 10:
                print("Эта позиция не существует")
            else:
                print("Эта позиция занята")


def game():
    field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    i = 0
    print_field(field)
    while not win(field):
        field = move(i, field)
        print_field(field)
        w = win(field)
        if w == 'X':
            return '\n\nКрестики выйграли!'
        elif w == '0':
            return '\n\nНолики выйграли!'
        elif w == 'n':
            return '\n\nНичья.'
        i += 1


print(game())
