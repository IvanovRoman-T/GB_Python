# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def binary(n):
    result = ''
    while n != 0:
        result += str(n % 2)
        n = n // 2
    return result[len(result)::-1]


num = int(input('Введите число: '))
print(f"Двоичная запись числа {num} - {binary(num)}")
