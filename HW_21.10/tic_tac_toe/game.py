# Создайте программу для игры в ""Крестики-нолики"".
import emoji


o = emoji.emojize(':red_circle:')
x = emoji.emojize(':cross_mark:')


# Создайте программу для игры в ""Крестики-нолики"".


def win(f):
    global x
    global o
    for i in f:
        if i == [x] * 3:
            return x
        elif i == [o] * 3:
            return o
    for i in list(zip(f[0], f[1], f[2]))[0]:
        if i == (x,) * 3:
            return x
        elif i == (o,) * 3:
            return o
    if f[0][0] == f[1][1] == f[2][2] == x or f[0][2] == f[1][1] == f[2][0] == x:
        return x
    elif f[0][0] == f[1][1] == f[2][2] == o or f[0][2] == f[1][1] == f[2][0] == o:
        return o
    for i in f:
        for j in i:
            if j != x and j != o:
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
    global x
    global o
    if not i % 2:
        while True:
            inp = int(input(emoji.emojize(f"Куда поставить {x}?   ")))
            if f[(inp - 1) // 3][inp % 3 - 1] != x and f[(inp - 1) // 3][inp % 3 - 1] != o:
                f[(inp - 1) // 3][inp % 3 - 1] = x
                return f
            if not 0 < inp < 10:
                print("Эта позиция не существует")
            else:
                print("Эта позиция занята")
    else:
        while True:
            inp = int(input(emoji.emojize(f"Куда поставить {o}?   ")))
            if f[(inp - 1) // 3][inp % 3 - 1] != x and f[(inp - 1) // 3][inp % 3 - 1] != o:
                f[(inp - 1) // 3][inp % 3 - 1] = o
                return f
            if not 0 < inp < 10:
                print("Эта позиция не существует")
            else:
                print("Эта позиция занята")


def game():
    global x
    global o
    field = [emoji.emojize(':keycap_1: :keycap_2: :keycap_3:').split(),
             emoji.emojize(':keycap_4: :keycap_5: :keycap_6:').split(),
             emoji.emojize(':keycap_7: :keycap_8: :keycap_9:').split()]
    i = 0
    print_field(field)
    while not win(field):
        field = move(i, field)
        print_field(field)
        w = win(field)
        if w == x:
            return emoji.emojize('\n\nКрестики выйграли! :trophy::party_popper::party_popper:')
        elif w == o:
            return emoji.emojize('\n\nНолики выйграли! :trophy::party_popper::party_popper:')
        elif w == 'n':
            return emoji.emojize('\n\nНичья. :handshake:')
        i += 1


print(game())
