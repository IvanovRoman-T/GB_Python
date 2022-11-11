def read_file(file_name='data.txt', t=1):
    with open(file_name, 'r') as file:
        data = set()
        a = file.readlines()
        for ind, el in enumerate(a):
            if el != '\n':
                if '\n' in el:
                    a[ind] = el[:len(el) - 1]
        if t == 1:
            for i in range(0, len(a), 5):
                if len(a[i:]) >= 4:
                    data.add(tuple(a[i:i + 4]))
        else:
            for i in a:
                data.add(tuple(i.split(', ')))
    return data


def write_file(data, file_name, t=1):
    with open(file_name, 'w') as file:
        if t == 1:
            for ind, person in enumerate(data):
                if ind == len(data) - 1:
                    for i, el in enumerate(person):
                        if i == len(person) - 1:
                            file.writelines(el)
                        else:
                            file.writelines(el + '\n')
                else:
                    for el in person:
                        file.writelines(el + '\n')
                    file.writelines('\n')
        else:
            for ind, person in enumerate(data):
                if ind == len(data) - 1:
                    file.writelines(', '.join(person))
                else:
                    file.writelines(', '.join(person) + '\n')
