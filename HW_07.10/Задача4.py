# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def compress(string):
    result = ''
    while string != '':
        a = string[0]
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                a += string[i + 1]
            else:
                break
            if i == 7:
                break
        result += f"{len(a)}{a[0]}"
        string = string[len(a):]
    return result


def unpack(string):
    result = ''
    for i in range(len(string) // 2):
        result += int(string[2 * i]) * string[2 * i + 1]
    return result


with open("ex4_input.txt", 'w') as file:
    file.writelines("qqqqwwwwwwwwweeeeeeeeeeerrrrrrrrtttyyyyyyuiiiiopp")
with open("ex4_input.txt", 'r') as file:
    str_ = file.readline()
c = compress(str_)
u = unpack(c)
with open("ex4_result.txt", 'w') as file:
    file.writelines("Сжатая строка: " + c + '\n')
    file.writelines("Распакованная строка: " + u)
