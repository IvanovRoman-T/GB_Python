from commands import command


authorized = False
while True:
    if not authorized:
        c = input("Введите {exit} для выхода из программы, {log in} для начала авторизации: ")
        authorized = command(c, authorized)
        if authorized == 'break':
            break
        elif authorized:
            command('help', authorized)
    else:
        c = input("Введите команду: ")
        a = command(c, authorized)
        if a == 'break':
            break
