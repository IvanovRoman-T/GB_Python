import data


def log_in():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login in data.passwords.keys():
        if data.passwords[login] == password:
            return login
        else:
            print("Неверный логин или пароль.")
            return False
    else:
        print("Неверный логин или пароль.")
        return False
