with open('passwords.txt', 'r') as file:
    passwords = {}
    for line in file.readlines():
        passwords[line[:line.find(',')]] = line[line.find(',') + 1:].replace('\n', '')


with open('database.txt', 'r') as file:
    database = {}
    for line in file.readlines():
        a = line[line.find(":") + 1:].split(',')
        inf = {"роль": a[0], "имя": a[3], "фамилия": a[2], "отчество": a[4].replace('\n', '')}
        if line[line.find(":") + 1] == 't':
            inf["предмет"] = a[1]
        else:
            inf["класс"] = a[1]
        database[line[:line.find(":")]] = inf


with open('homework.txt', 'r') as file:
    homework = {}
    for line in file.readlines():
        a = line[line.find(":") + 1:].split(';')
        exercise = {}
        for date in a:
            exercise[date[:5]] = date[5:].replace('\n', '')
        homework[line[:line.find(":")]] = exercise


def save():
    with open('homework.txt', 'w') as file:
        for i, subject in enumerate(homework.keys()):
            string = subject + ':'
            for ind, date in enumerate(homework[subject].keys()):
                string += f"{date}{homework[subject][date]}"
                if ind != len(homework[subject].keys()) - 1:
                    string += ';'
            if i != len(homework.keys()) - 1:
                string += '\n'
            file.writelines(string)
